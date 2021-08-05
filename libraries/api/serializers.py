from rest_framework import serializers
from users.api.serializers import AccountSerializer
from workbooks.api.serializers import WorkbookSerializer
from ..models import Library

class LibrarySerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    workbooks = WorkbookSerializer(many=True)

    class Meta:
        model = Library
        fields = ['id', 'owner', 'workbooks', 'created', 'modified',]
