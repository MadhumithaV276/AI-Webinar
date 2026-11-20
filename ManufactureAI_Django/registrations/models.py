from django.db import models

class Registration(models.Model):
    ROLE_CHOICES = [
        ("Manufacturing professional", "Manufacturing professional"),
        ("Plant / Operations Manager", "Plant / Operations Manager"),
        ("Engineer / Technician", "Engineer / Technician"),
        ("Business owner", "Business owner"),
        ("Student", "Student"),
        ("Faculty / Trainer", "Faculty / Trainer"),
        ("Other", "Other"),
    ]
    EXPERIENCE_CHOICES = [("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced")]
    TICKET_CHOICES = [("Early Bird - ₹299", "Early Bird - ₹299"), ("Regular - ₹499", "Regular - ₹499")]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=18)
    organization = models.CharField(max_length=150)
    role = models.CharField(max_length=60, choices=ROLE_CHOICES)
    industry = models.CharField(max_length=80, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    ticket = models.CharField(max_length=40, choices=TICKET_CHOICES)
    expectations = models.TextField(blank=True, max_length=1000)
    consent = models.BooleanField(default=False)
    webinar = models.CharField(max_length=120, default="AI for Manufacturing")
    webinar_date = models.CharField(max_length=50, default="10 December 2026")
    webinar_time = models.CharField(max_length=60, default="2:00 PM - 4:00 PM IST")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.email})"
