from rest_framework import serializers
from ..models import Embed, Image

from users.api import serializers as account_serializers


class EmbedSerializer(serializers.ModelSerializer):
    owner = account_serializers.AccountSerializer(read_only=True)

    class Meta:
        model = Embed
        fields = ['id', 'owner', 'archived', 'created', 'modified', 'title', 'embed',]


class ImageSerializer(serializers.ModelSerializer):
    owner = account_serializers.AccountSerializer(read_only=True)
    
    class Meta:
        model = Image
        fields = ['id', 'owner', 'archived', 'created', 'modified', 'title', 'featured', 'image']
