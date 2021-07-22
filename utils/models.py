from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

class Core(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)ss')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @cached_property
    def formatted_created(self):
        return self.created.strftime("%m/%d/%y %I:%M %p")

    @cached_property
    def formatted_modified(self):
        if self.modified:
            return self.modified.strftime("%m/%d/%y %I:%M %p")