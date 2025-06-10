from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Company, Job, Resume, Application
from . import serializers
from .permissions import ReadOnly, IsOwnerOrReadOnly, IsAdminOrOwner


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
        serializer.save(user=self.request.user)


class ApplicationViewset(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]

    def get_queryset(self):
        return self.queryset.filter(
            Q(user=self.request.user) | Q(job__posted_by__is_admin=True)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
