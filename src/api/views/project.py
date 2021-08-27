from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.project import ProjectCompactSerializer, ProjectSerializer
from core.models import Project


class ProjectViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    def get_serializer_class(self):
        if self.action in ("list",):
            return ProjectCompactSerializer
        else:
            return ProjectSerializer
