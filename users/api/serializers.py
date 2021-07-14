from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import Group
from users.models import Account

from dj_rest_auth.registration.serializers import RegisterSerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']


class GroupSerializer(serializers.ModelSerializer):
    user_set = AccountSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'user_set',]


class WFRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user