from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["task_id", "user", "title", "description", "creation_time", "deadline", "status"]

class TaskModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["user", "title", "description", "creation_time", "deadline", "status"]