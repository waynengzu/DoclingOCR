from rest_framework import serializers
from store.models import User, Document, Log


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name', 'type', 'path', 'user')

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'created_at', 'document')