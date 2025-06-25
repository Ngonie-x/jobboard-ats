from rest_framework import serializers

from .models import Company, Job, Resume, Application


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "company-detail", "lookup_field": "pk"}}


class JobSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Job
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "job-detail", "lookup_field": "pk"}}


class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Resume
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "resume-detail", "lookup_field": "pk"}}


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "application-detail", "lookup_field": "pk"}
        }
