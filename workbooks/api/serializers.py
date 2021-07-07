from rest_framework import serializers
from ..models import Workbook, Chapter, Page


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified']


class ChapterSerializer(serializers.ModelSerializer):
    page_set = PageSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'page_set']


class WorkbookSerializer(serializers.ModelSerializer):
    chapter_set = ChapterSerializer(many=True)

    class Meta:
        model = Workbook
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'chapter_set']