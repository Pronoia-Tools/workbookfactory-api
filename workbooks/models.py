from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose
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
    language = models.CharField(max_length=100, blank=True, null=True)
    edition = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True)
    tags = TaggableManager()
    cover_image = models.ImageField(upload_to="images", null=True)
    cover_image_thumbnail = ImageSpecField(source='cover_image',
                                           processors=[
                                               Transpose(),
                                               ResizeToFill(150, 150)
                                            ],
                                           format='JPEG',
                                           options={'quality': 40})
    cover_image_card = ImageSpecField(source='cover_image',
                                            processors=[
                                                Transpose(),
                                                ResizeToFill(512, 512)
                                            ],
                                            format='JPEG',
                                            options={'quality': 60})
    
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


class Question(Core):
    question = models.CharField(max_length=200)
    chapter = models.ManyToManyField('Chapter', blank=True)

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