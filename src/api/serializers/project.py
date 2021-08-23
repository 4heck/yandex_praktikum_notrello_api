from rest_framework import serializers

from api.serializers.column import ColumnSerializer
from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    columns = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "columns",
        )

    def get_columns(self, obj):
        return ColumnSerializer(obj.columns.all(), many=True).data


class ProjectCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
        )
