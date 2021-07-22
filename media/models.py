import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose
from utils.models import Core

# Create your models here.
class Embed(Core):
    title = models.CharField(max_length=255)
    embed = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Embed"
        verbose_name_plural = "Embeds"

class Image(Core):
    title = models.CharField(max_length=255, null=True, blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                           processors=[
                                               Transpose(),
                                               ResizeToFill(150, 150)],
                                           format='JPEG',
                                           options={'quality': 40})
    image_card = ImageSpecField(source='image',
                                            processors=[
                                                Transpose(),
                                                ResizeToFill(512, 512)],
                                            format='JPEG',
                                            options={'quality': 60})
    image_hero = ImageSpecField(source='image',
                                      processors=[
                                          Transpose(),
                                          ResizeToFill(1440, 810)],
                                      format='JPEG',
                                      options={'quality': 60})

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['-created']

    def filename(self):
        return os.path.basename(self.image.name)

    def save(self, *args, **kwargs):
        self.title = os.path.basename(self.image.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
