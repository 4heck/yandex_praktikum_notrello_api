from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.task import TaskSerializer
from core.models import Task

# from rest_framework.response import Response
# from rest_framework.decorators import action


class TaskViewSet(
    GenericViewSet,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    # @action(detail=True, url_path="update-position")
    # def update_position(self, request, pk):
    #     # TODO: написать код оптимизированного обновления позиций
    #     return Response(pk)
