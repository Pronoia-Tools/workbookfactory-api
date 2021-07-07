from django.db import models
from django.utils.text import slugify
from utils.models import Core

# Create your models here.
class Workbook(Core):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='', blank=True)
    front_matter = models.TextField(blank=True)
    back_matter = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Workbook"
        verbose_name_plural = "Workbooks"

class Chapter(Core):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='', blank=True)
    front_matter = models.TextField(blank=True)
    back_matter = models.TextField(blank=True)
    content = models.TextField(blank=True)
    workbook = models.ManyToManyField('Workbook', blank=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"