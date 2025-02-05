from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Document
from .serializers import UserSerializer, DocumentSerializer


# Create your views here.
@api_view()
def user_list(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view()
def document_list(request):
    queryset = Document.objects.all()
    serializer = DocumentSerializer(queryset, many=True)
    return Response (serializer.data)