from rest_framework import serializers

from api.serializers.task import TaskSerializer
from core.models import Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ("id", "title", "position", "project")


class ColumnCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ("id", "title", "position")


class ColumnTasksSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Column
        fields = ("id", "title", "position", "tasks")
