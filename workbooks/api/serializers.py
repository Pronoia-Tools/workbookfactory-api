from rest_framework import serializers
from django.contrib.auth.models import Group
from ..models import Workbook

class WorkbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workbook
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified']