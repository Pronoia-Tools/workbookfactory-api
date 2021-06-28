from rest_framework import serializers
from django.contrib.auth.models import Group
from users.models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']


class GroupSerializer(serializers.ModelSerializer):
    user_set = AccountSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'user_set',]