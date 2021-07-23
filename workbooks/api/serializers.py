from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from ..models import Workbook, Chapter, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'owner', 'answer', 'archived', 'created', 'modified']


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'owner', 'question', 'archived', 'created', 'modified', 'answer_set']


class ChapterSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Chapter
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'question_set']


class WorkbookSerializer(serializers.ModelSerializer):
    chapter_set = ChapterSerializer(many=True, required=False)
    price = MoneyField(max_digits=10, decimal_places=2)

    class Meta:
        model = Workbook
        fields = ['id', 'owner', 'title', 'price', 'edition', 'language', 'description', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'chapter_set', 'published', 'editable']