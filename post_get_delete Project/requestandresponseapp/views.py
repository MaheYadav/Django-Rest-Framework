from rest_framework.decorators import api_view
from rest_framework.response import Response
from requestandresponseapp.models import subject
from requestandresponseapp.serializers import SubjectSerializer
from rest_framework import status
from rest_framework import serializers

# @api_view(['GET'])
# def ApiOverview(request):
# 	api_urls = {
# 		'all_items': '/',
# 		'Search by Category': '/?category=category_name',
# 		'Search by Subcategory': '/?subcategory=category_name',
# 		'Add': '/create',
# 		'Update': '/update/pk',
# 		'Delete': '/item/pk/delete'
# 	}

# 	return Response(api_urls)


      

@api_view(['POST'])
def post_subject(request):
	if request.method == 'POST':
		serializer = SubjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_subject(request):
	if request.method == 'GET':
		sub=subject.objects.all()
		serializer = SubjectSerializer(sub, many=True)
		return Response(serializer.data)

@api_view(['DELETE'])
def delete_subject(request,pk):
	if request.method == 'DELETE':
		sub=subject.objects.all()
		sub.delete()
		return Response(status=status.HTTP_202_ACCEPTED)

