from django.db import models

from core.models.mixins import BaseModelMixin


class Project(BaseModelMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
