from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

from ..models import Image, Embed
from . import serializers


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # this will associate the owner of the object with the session user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EmbedViewSet(viewsets.ModelViewSet):
    queryset = Embed.objects.all()
    serializer_class = serializers.EmbedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # this will associate the owner of the object with the session user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)