from rest_framework import serializers
from django.contrib.auth.models import Group
from ..models import Workbook, Chapter


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified']


class WorkbookSerializer(serializers.ModelSerializer):
    chapter_set = ChapterSerializer(many=True)

    class Meta:
        model = Workbook
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'chapter_set']