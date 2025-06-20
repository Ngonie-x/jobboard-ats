import tempfile, os
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Company, Job, Resume, Application
from . import serializers
from .permissions import ReadOnly, IsOwnerOrReadOnly, IsAdminOrOwner
from .utils.resume import extract_resume_sections_from_pdf


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "location", "job_type"]


class ResumeViewset(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = serializers.ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        pdf = self.request.FILES.get("file")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            for chunk in pdf.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name

        try:
            pdf_sections = extract_resume_sections_from_pdf(tmp_path)
        finally:
            os.unlink(tmp_path)
        print(pdf_sections)
        serializer.save(user=self.request.user, parsed_data=pdf_sections)


class ApplicationViewset(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]

    def get_queryset(self):
        return self.queryset.filter(
            Q(user=self.request.user) | Q(job__posted_by__is_staff=True)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Check if a new file is being uploaded
        if "file" in serializer.validated_data:
            uploaded_file = serializer.validated_data.get("file")
            pdf_sections = extract_resume_sections_from_pdf(uploaded_file)
            serializer.save(parsed_data=pdf_sections)
        else:
            # No new file, just save other changes
            serializer.save()
