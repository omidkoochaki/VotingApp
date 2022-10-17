
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import RegisterSerializer, UserDetailsSerializer


class RegisterView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserDetailViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin,):
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDetailsSerializer


