from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.column import (
    ColumnCompactSerializer,
    ColumnSerializer,
    ColumnTasksSerializer,
)
from core.models import Column


class ColumnViewSet(
    GenericViewSet,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = Column.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "patch", "delete", "head", "options", "trace"]

    def get_serializer_class(self):
        if self.action in ("create",):
            return ColumnSerializer
        elif self.action in ("retrieve",):
            return ColumnTasksSerializer
        else:
            return ColumnCompactSerializer
