from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from viewsetapp.models import UserRegistration
from viewsetapp.serializer import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = UserRegistration.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = UserRegistration.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)