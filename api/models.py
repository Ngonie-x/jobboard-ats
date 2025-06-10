from django.db import models
from django.contrib.auth import get_user_model


class Company(models.Model):
    name = models.CharField(max_length=52)
    description = models.TextField()
    logo = models.ImageField(upload_to="logos/")
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
        ("Internship", "Internship"),
        ("Temporary", "Temporary"),
        ("Freelance", "Freelance"),
        ("Remote", "Remote"),
        ("Hybrid", "Hybrid"),
    ]

    title = models.CharField(max_length=52)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField()
    job_type = models.CharField(
        max_length=20, choices=JOB_TYPE_CHOICES, default="Full-time"
    )
    salary_range = models.CharField(max_length=20)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=False)
    expired_at = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.company}"


class Resume(models.Model):
    user = models.OneToOneField(get_user_model(), models.CASCADE)
    file = models.FileField(upload_to="resumes/")
    parsed_data = models.JSONField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Reviewed", "Reviewed"),
        ("Interviewing", "Interviewing"),
        ("Rejected", "Rejected"),
        ("Offered", "Offered"),
        ("Hired", "Hired"),
        ("Withdrawn", "Withdrawn"),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    cover_letter = models.FileField(upload_to="cover_letters/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Applied")
    applied_at = models.DateTimeField(auto_now_add=True)
