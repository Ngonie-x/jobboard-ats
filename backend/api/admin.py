from django.contrib import admin

from .models import Company, Job, Resume, Application


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "website"]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "location", "job_type"]
    list_filter = ["company", "job_type"]


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["user", "uploaded_at"]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["job", "user", "status", "applied_at"]
