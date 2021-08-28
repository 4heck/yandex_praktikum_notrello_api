from rest_framework import serializers

from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ("is_archived",)


class TaskUpdatePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("position",)
