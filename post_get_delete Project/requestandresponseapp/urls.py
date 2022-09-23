
from django.urls import path
from requestandresponseapp import views

urlpatterns = [
	# path('', views.ApiOverview, name='home'),
	path('post/', views.post_subject),
	path('get/',views.get_subject, name='getsub'),
	path('sub/<int:pk>/delete/', views.delete_subject, name='deletesubject'),
      
]


