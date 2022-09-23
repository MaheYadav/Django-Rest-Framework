from classbasedviewapp.models import subject
from rest_framework import serializers
class subjectserializer(serializers.ModelSerializer):
	class Meta:
		model = subject
		fields = '__all__'