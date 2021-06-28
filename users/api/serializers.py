from rest_framework import serializers

from users.models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']