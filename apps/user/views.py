from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class ToggleUserActiveView(UpdateAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status.HTTP_200_OK)


class ToggleUserStaffView(UpdateAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user.is_staff = not user.is_staff
        user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status.HTTP_200_OK)
