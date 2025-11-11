from django.urls import path

from .views import (
    AddUserToAdminView,
    BlockUserView,
    DelUserWithAdminView,
    SendEmailTestView,
    UnBlockUserView,
    UserListCreateView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/block', BlockUserView.as_view(), name='block_user'),
    path('/<int:pk>/un_block', UnBlockUserView.as_view(), name='un_block_user'),
    path('/<int:pk>/add_admin', AddUserToAdminView.as_view(), name='add_admin_user'),
    path('/<int:pk>/del_admin', DelUserWithAdminView.as_view(), name='del_admin_user'),
    path('/test', SendEmailTestView.as_view(), name='test_email'),
]
