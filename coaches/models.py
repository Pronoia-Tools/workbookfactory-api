from django.db import models
from django.utils.text import slugify
from utils.models import Core

# Create your models here.
class Coach(Core):
    clients = models.ManyToManyField('users.Account', blank=True, related_name="coach_clients")
    workbooks = models.ManyToManyField('workbooks.Workbook', blank=True)
    authors = models.ManyToManyField('users.Account', blank=True, related_name="coach_authors")

    def __str__(self):
        return '%s %s' % (self.owner.first_name, self.owner.last_name)

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"
