from rest_framework import serializers

from api.serializers.column import ColumnSerializer
from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "columns",
        )


class ProjectCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
        )
