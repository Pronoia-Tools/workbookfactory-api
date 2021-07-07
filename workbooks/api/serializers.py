from rest_framework import serializers
from ..models import Workbook, Chapter, Page, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'owner', 'answer', 'archived', 'created', 'modified']


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'owner', 'question', 'archived', 'created', 'modified', 'answer_set']


class PageSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Page
        fields = ['id', 'owner', 'title', 'slug', 'front_matter', 'back_matter', 'content', 'archived', 'created', 'modified', 'question_set']


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