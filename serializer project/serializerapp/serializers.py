from serializerapp.models import Jio
from rest_framework import serializers

class JioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jio
        fields = ['mobile_number']