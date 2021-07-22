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
    image_thumbnail_url = serializers.SerializerMethodField('get_image_thumbnail')
    image_card_url = serializers.SerializerMethodField('get_image_card')
    image_hero_url = serializers.SerializerMethodField('get_image_hero')

    class Meta:
        model = Image
        fields = ['id', 'owner', 'archived', 'created', 'modified', 'title', 'featured', 'image', 'image_thumbnail_url', 'image_card_url', 'image_hero_url']

    def get_image_thumbnail(self, obj):
        return obj.image_thumbnail.url

    def get_image_card(self, obj):
        return obj.image_card.url

    def get_image_hero(self, obj):
        return obj.image_hero.url