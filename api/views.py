from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Company, Job, Resume, Application
from . import serializers
from .permissions import ReadOnly, IsOwnerOrReadOnly


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class ResumeViewset(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = serializers.ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ApplicationViewset(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
