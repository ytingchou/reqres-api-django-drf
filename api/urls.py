from django.urls import path

from .views import (
    UserListView,
    UserRetrieveUpdateDestroyView,
    ResourceListView,
    ResourceRetrieveView,
    RegisterView,
    LoginView,
)

app_name = 'api'

urlpatterns = [
    path('users', UserListView.as_view(), name='user-list-api'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy-api'),
    path('unknown', ResourceListView.as_view(), name='resource-list-api'),
    path('unknown/<int:pk>', ResourceRetrieveView.as_view(), name='resource-retrieve-api'),
    path('register', RegisterView.as_view(), name='regiser-api'),
    path('login', LoginView.as_view(), name='login-api'),
]