from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from users.api.serializers import AccountSerializer
from ..models import Workbook, Chapter, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'owner', 'answer', 'archived', 'created', 'modified']


class QuestionSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    answer_set = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'owner', 'question', 'archived', 'created', 'modified', 'answer_set']


class ChapterSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    question_set = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Chapter
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'question_set']


class WorkbookSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    owner = AccountSerializer(read_only=True)
    chapter_set = ChapterSerializer(many=True, required=False)
    price = MoneyField(max_digits=10, decimal_places=2)
    cover_image_thumbnail_url = serializers.SerializerMethodField('get_cover_image_thumbnail')
    cover_image_card_url = serializers.SerializerMethodField('get_cover_image_card')

    class Meta:
        model = Workbook
        fields = [
            'id', 
            'owner', 
            'title', 
            'tags', 
            'price', 
            'edition', 
            'language', 
            'description',
            'slug',
            'front_matter',
            'back_matter',
            'content',
            'archived',
            'created',
            'modified',
            'chapter_set',
            'published',
            'editable',
            'cover_image',
            'cover_image_thumbnail_url',
            'cover_image_card_url'
        ]

    def get_cover_image_thumbnail(self, obj):
        if obj.cover_image_thumbnail:
            return obj.cover_image_thumbnail.url

    def get_cover_image_card(self, obj):
        if obj.cover_image_thumbnail:
            return obj.cover_image_thumbnail.url