from django.db.models import fields
from rest_framework import serializers
from requestandresponseapp.models import subject

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model  = subject
		fields =  '__all__'