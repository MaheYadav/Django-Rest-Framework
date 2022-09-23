from django.shortcuts import render
from parserapp.models import UserRegistration
from parserapp.serializer import UserSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.
class UserReg(APIView):
    """
    List all code UserRegistration, or create a new UserRegistration.
    """
    def get(self,request):
        ur=UserRegistration.objects.all()
        serializer = UserSerializer(ur, many=True)
        return Response(serializer.data)
    parser_classes = [JSONParser]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse(serializer.data, status=201, content_type='application/json')
