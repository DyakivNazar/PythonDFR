from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class BlockUserView(UpdateAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status.HTTP_200_OK)


class UnBlockUserView(UpdateAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status.HTTP_200_OK)


class AddUserToAdminView(UpdateAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = True
            user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status.HTTP_200_OK)


class DelUserWithAdminView(UpdateAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = True
            user.save()
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status.HTTP_200_OK)
