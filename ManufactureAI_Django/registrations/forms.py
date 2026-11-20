from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    consent = forms.BooleanField(required=True, error_messages={"required": "Please accept the consent to register."})

    class Meta:
        model = Registration
        fields = ["full_name", "email", "phone", "organization", "role", "industry", "experience", "ticket", "expectations", "consent"]
        widgets = {
            "full_name": forms.TextInput(attrs={"maxlength": 100}),
            "email": forms.EmailInput(attrs={"maxlength": 150}),
            "phone": forms.TextInput(attrs={"maxlength": 18}),
            "organization": forms.TextInput(attrs={"maxlength": 150}),
            "expectations": forms.Textarea(attrs={"maxlength": 1000}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        duplicates = Registration.objects.filter(email__iexact=email, webinar="AI for Manufacturing")
        if self.instance.pk:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise forms.ValidationError("This email address is already registered for this webinar.")
        return email
