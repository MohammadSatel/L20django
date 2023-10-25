from rest_framework import serializers
from .models import Task
from rest_framework.views import APIView


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'