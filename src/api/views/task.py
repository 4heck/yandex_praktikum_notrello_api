from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers.task import TaskSerializer, TaskUpdatePositionSerializer
from api.services.task import register_task_update_position
from core.models import Task


class TaskViewSet(
    GenericViewSet,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    def get_serializer_class(self):
        if self.action in ("update_position",):
            return TaskUpdatePositionSerializer
        else:
            return TaskSerializer

    @swagger_auto_schema(
        operation_summary="Берем таску сверху, таску снизу, складываем их позиции и делим пополам."
        " Получившееся значение отправляем в этот эндпоинт"
    )
    @action(detail=True, url_path="update-position", methods=["PATCH"])
    def update_position(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        position = request.data.get("position")
        task.position = position
        task.save()

        register_task_update_position(task, position)

        return Response(TaskSerializer(task).data)
