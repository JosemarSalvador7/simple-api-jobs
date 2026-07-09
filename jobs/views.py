from rest_framework.viewsets import ModelViewSet
from jobs.models import Job
from jobs.serializers import JobSerializer


class JobView(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
