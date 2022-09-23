from django.urls import  path,include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user',UserViewSet,basename='UserViewSet')
urlpatterns = [
     path('', include(router.urls)),
]


# Using include with routers

# Alternatively you can use Django's include function, like so.
#
#
# urlpatterns = [
#     path('forgot-password', ForgotPasswordFormView.as_view()),
#     path('', include(router.urls)),
# ]

