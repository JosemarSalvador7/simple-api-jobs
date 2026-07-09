from rest_framework.serializers import ModelSerializer
from jobs.models import Job


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
