from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

from ..models import Workbook, Chapter, Page
from . import serializers

class WorkbookViewSet(viewsets.ModelViewSet):
    queryset = Workbook.objects.all()
    serializer_class = serializers.WorkbookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content',]

    # this will associate the owner of the object with the session user
    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content',]

    # this will associate the owner of the object with the session user
    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content',]

    # this will associate the owner of the object with the session user
    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)