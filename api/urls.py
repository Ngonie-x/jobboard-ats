from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"companies", views.CompanyViewset, basename="company")
router.register(r"jobs", views.JobViewset, basename="job")
router.register(r"resumes", views.ResumeViewset, basename="resume")
router.register(r"applications", views.ApplicationViewset, basename="application")

urlpatterns = router.urls
