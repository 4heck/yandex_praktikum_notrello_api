from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.project import ProjectSerializer
from core.models import Project


class ProjectViewSet(GenericViewSet, ListModelMixin):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated,)
