from rest_framework.viewsets import ModelViewSet
from skills.models import Skill
from skills.serializers import SkillSerializer

# FAZ O MESMO QUE ESSE


class SkillView(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
