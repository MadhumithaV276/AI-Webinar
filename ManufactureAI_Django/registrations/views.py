import csv
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import RegistrationForm
from .models import Registration

def webinar(request):
    return render(request, "webinar.html")

def register(request):
    if request.method != "POST":
        return redirect("webinar")
    form = RegistrationForm(request.POST)
    if form.is_valid():
        registration = form.save(commit=False)
        registration.webinar = "AI for Manufacturing"
        registration.webinar_date = "10 December 2026"
        registration.webinar_time = "2:00 PM - 4:00 PM IST"
        registration.save()
        request.session["last_registration_name"] = registration.full_name
        return redirect("registration_success")
    return render(request, "registration_error.html", {"form": form}, status=400)

def registration_success(request):
    name = request.session.pop("last_registration_name", "")
    return render(request, "success.html", {"name": name})

@staff_member_required
def dashboard(request):
    query = request.GET.get("q", "").strip()
    ticket = request.GET.get("ticket", "").strip()
    registrations = Registration.objects.all()
    if query:
        registrations = registrations.filter(
            Q(full_name__icontains=query) | Q(email__icontains=query) |
            Q(phone__icontains=query) | Q(organization__icontains=query)
        )
    if ticket:
        registrations = registrations.filter(ticket=ticket)
    context = {
        "registrations": registrations,
        "total_count": Registration.objects.count(),
        "early_count": Registration.objects.filter(ticket__icontains="Early Bird").count(),
        "regular_count": Registration.objects.filter(ticket__icontains="Regular").count(),
        "query": query, "selected_ticket": ticket,
    }
    return render(request, "registrations/dashboard.html", context)

@staff_member_required
def edit_registration(request, pk):
    item = get_object_or_404(Registration, pk=pk)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=item)
        # Editing should allow the current email to remain unchanged.
        if form.is_valid():
            form.save()
            messages.success(request, "Registration updated.")
            return redirect("dashboard")
    else:
        form = RegistrationForm(instance=item)
    return render(request, "registrations/edit.html", {"form": form, "item": item})

@staff_member_required
def delete_registration(request, pk):
    item = get_object_or_404(Registration, pk=pk)
    if request.method == "POST":
        item.delete()
        messages.success(request, "Registration deleted.")
    return redirect("dashboard")

@staff_member_required
def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="webinar_registrations.csv"'
    writer = csv.writer(response)
    writer.writerow(["Timestamp", "Full name", "Email", "Phone", "Organization", "Role", "Industry", "AI experience", "Ticket", "Expectations"])
    for r in Registration.objects.all():
        writer.writerow([timezone.localtime(r.created_at).strftime("%Y-%m-%d %H:%M"), r.full_name, r.email, r.phone, r.organization, r.role, r.industry, r.experience, r.ticket, r.expectations])
    return response
