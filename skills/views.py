from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from skills.serializers import SkillSerializer
from skills.models import Skill
from rest_framework import status
# from typing import


class SkillListView(APIView):
    def get(self, request):
        serializer = SkillSerializer(Skill.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillDetailView(APIView):
    def get(self, requests, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def delete(self, requests, pk):
        skill = get_object_or_404(Skill, pk=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, requests, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill, requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
