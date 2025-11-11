import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminUser,)



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


class SendEmailTestView(GenericAPIView):
    def get(self,*args, **kwargs):
        template = get_template('test_email.html')
        html_content = template.render({'name': 'Django'})
        msg = EmailMultiAlternatives(
            subject='Test Email',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=['test@gmail.com']
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return Response({'message': 'Email sent!'}, status.HTTP_200_OK)
