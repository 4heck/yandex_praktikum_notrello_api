from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from api.views.column import ColumnViewSet
from api.views.project import ProjectViewSet
from api.views.task import TaskViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="NoTrello API",
        default_version="v1",
        description="Yandex Praktikum",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mamleev.rus@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

router = SimpleRouter()

router.register("project", ProjectViewSet, basename="project")
router.register("column", ColumnViewSet, basename="column")
router.register("task", TaskViewSet, basename="column")

urlpatterns += router.urls
