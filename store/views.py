from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Document, Log
from .serializers import UserSerializer, DocumentSerializer, LogSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')

@api_view(['GET', 'PUT'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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