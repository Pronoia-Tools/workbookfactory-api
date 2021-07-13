from rest_framework import serializers
from ..models import Coach

from workbooks.api import serializers as workbook_serializers
from users.api import serializers as account_serializers


class CoachSerializer(serializers.ModelSerializer):
    authors = account_serializers.AccountSerializer(many=True)
    clients = account_serializers.AccountSerializer(many=True)
    workbooks = workbook_serializers.WorkbookSerializer(many=True)

    class Meta:
        model = Coach
        fields = ['id', 'owner', 'archived', 'created', 'modified', 'authors', 'clients', 'workbooks',]
