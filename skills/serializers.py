from rest_framework.serializers import ModelSerializer
from skills.models import Skill


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ("id", "name")
