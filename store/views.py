from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, viewsets
from .models import User, Document, Log
from .serializers import UserSerializer, DocumentSerializer, LogSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def delete(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LogViewSet(ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def delete(self, request, pk):
        log = get_object_or_404(Log, pk=pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
