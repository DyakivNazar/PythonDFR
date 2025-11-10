from django.urls import path

from .views import ToggleUserActiveView, ToggleUserStaffView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/change_active', ToggleUserActiveView.as_view(), name='toggle_active_user'),
    path('/<int:pk>/change_staff', ToggleUserStaffView.as_view(), name='toggle_staff_user'),
]