from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from registrations import views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("", views.webinar, name="webinar"),
    path("register/", views.register, name="register"),
    path("registration-success/", views.registration_success, name="registration_success"),
    path("admin-login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("admin-logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/registration/<int:pk>/edit/", views.edit_registration, name="edit_registration"),
    path("dashboard/registration/<int:pk>/delete/", views.delete_registration, name="delete_registration"),
    path("dashboard/export.csv", views.export_csv, name="export_csv"),
]
