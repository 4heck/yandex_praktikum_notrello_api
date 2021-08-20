from django.db import models

from core.models.mixins import BaseModelMixin
from core.models.project import Project


class Column(BaseModelMixin):
    title = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.project})"

    class Meta:
        ordering = ["position"]
