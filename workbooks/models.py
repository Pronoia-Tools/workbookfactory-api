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
    published = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)

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


class Page(Core):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='', blank=True)
    front_matter = models.TextField(blank=True)
    back_matter = models.TextField(blank=True)
    content = models.TextField(blank=True)
    chapter = models.ManyToManyField('Chapter', blank=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class Question(Core):
    question = models.CharField(max_length=200)
    page = models.ManyToManyField('Page', blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(Core):
    answer = models.CharField(max_length=200)
    question = models.ManyToManyField('Question', blank=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"