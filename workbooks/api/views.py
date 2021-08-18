from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets, parsers
from rest_framework import filters

from utils import permissions as wf_permissions

from ..models import Workbook, Chapter, Question, Answer
from . import serializers


class PublicWorkbookViewSet(viewsets.ModelViewSet):
    queryset = Workbook.objects.all()
    serializer_class = serializers.WorkbookSerializer
    permission_classes = [wf_permissions.ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'title', 'content',]


class OwnerWorkbookViewSet(viewsets.ModelViewSet):
    queryset = Workbook.objects.all()
    serializer_class = serializers.WorkbookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'title', 'content',]

    # this will associate the owner of the object with the session user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class PublicChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
    permission_classes = [wf_permissions.ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'title', 'content',]


class OwnerChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'title', 'content',]

    # this will associate the owner of the object with the session user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class PublicQuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [wf_permissions.ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'question',]


class OwnerQuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'question',]

    # this will associate the owner of the object with the session user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class OwnerAnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__id', 'answer',]

    # this will associate the owner of the object with the session user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset