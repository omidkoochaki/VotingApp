from django.urls import path
from rest_framework import routers

from users.views import RegisterView, UserDetailViewSet


router = routers.DefaultRouter()
router.register(prefix='signup', viewset=RegisterView, basename='user-signup')
router.register(prefix='details', viewset=UserDetailViewSet, basename='user')

user_urls = router.urls

