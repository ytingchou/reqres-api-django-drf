from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import (
    UserModel,
    ResourceModel,
)
from .serializers import (
    UserUpdateSerializer,
    RegisterSerializer,
    LoginSerializer,
)
from .pagination import ListPagination


class UserListView(APIView):
    def get(self, request, format=None):
        users = UserModel.all()

        paginator = ListPagination()
        page = paginator.paginate_queryset(users, request)
        return paginator.get_paginated_response(page)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk, format=None):
        users = UserModel.all()
        for user in users:
            if int(pk) == user['id']:
                return Response(data={
                    "data": user,
                })
        return Response(data={}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data={
            **serializer.data,
            'updated_at': timezone.now(),
        })

    def patch(self, request, pk, format=None):
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data={
            **serializer.data,
            'updated_at': timezone.now(),
        })

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResourceListView(APIView):
    def get(self, request, format=None):
        resources = ResourceModel.all()

        paginator = ListPagination()
        page = paginator.paginate_queryset(resources, request)
        return paginator.get_paginated_response(page)


class ResourceRetrieveView(APIView):
    def get(self, request, pk, format=None):
        resources = ResourceModel.all()
        for resource in resources:
            if int(pk) == resource['id']:
                return Response(data={
                    "data": resource,
                })
        return Response(data={}, status=status.HTTP_404_NOT_FOUND)


class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id = 4
        token = Token.generate_key()
        return Response({
            'id': id,
            'token': token,
        })


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = Token.generate_key()
        return Response({
            'token': token,
        })
