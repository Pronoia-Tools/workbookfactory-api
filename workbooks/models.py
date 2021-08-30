import os
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
import djstripe
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose
from utils.models import Core
from django.utils.functional import cached_property

# Create your models here.
class Workbook(Core):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='', blank=True)
    front_matter = models.TextField(blank=True)
    back_matter = models.TextField(blank=True)
    content = models.JSONField(blank=True, default={})
    published = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    language = models.CharField(max_length=100, blank=True, null=True)
    edition = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True)
    tags = TaggableManager()
    cover_image = models.ImageField(upload_to="images", null=True)
    stripe_product = models.ForeignKey(djstripe.models.Product, on_delete=CASCADE, null=True)
    stripe_price = models.ForeignKey(djstripe.models.Price, on_delete=CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Workbook"
        verbose_name_plural = "Workbooks"

    def filename(self):
        return os.path.basename(self.image.name)
    
    def __str__(self):
        return self.title

    @cached_property
    def cached_stripe_product_id(self):
        return self.stripe_product.id

    @cached_property
    def cached_stripe_price_id(self):
        return self.stripe_price.id

class Chapter(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, default='', blank=True)
    content = models.TextField(blank=True)
    workbook = models.ForeignKey(Workbook, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    @cached_property
    def formatted_created(self):
        return self.created.strftime("%m/%d/%y %I:%M %p")

    @cached_property
    def formatted_modified(self):
        if self.modified:
            return self.modified.strftime("%m/%d/%y %I:%M %p")


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