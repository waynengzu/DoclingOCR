from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Document, Log
from .serializers import UserSerializer, DocumentSerializer, LogSerializer

# Create your views here.

class UserList(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')

class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, id):
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        user = get_object_or_404(User, pk=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def document_list(request):
    if request.method == 'GET':
        queryset = Document.objects.all()
        serializer = DocumentSerializer(queryset, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view()
def log_list(request):
    queryset = Log.objects.all()
    serializer = LogSerializer(queryset, many=True)
    return Response(serializer.data)