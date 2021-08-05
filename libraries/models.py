from django.db import models
from utils.models import Core

# Create your models here.
class Library(Core):
    workbooks = models.ManyToManyField("workbooks.Workbook")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"
