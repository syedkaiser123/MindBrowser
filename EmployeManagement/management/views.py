from django.shortcuts import render
from management.models import Manager, Employee
from rest_framework import viewsets
from api.utils.permissions import AccountsManagementPermission
from api import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeSerializer
    permission_classes = [AccountsManagementPermission]
    http_method_names = ['get', 'post', 'delete', 'put',]

    def get_serializer_class(self, *args, **kwargs):

        if self.action == 'list':
            return serializers.EmployeGetSerializer

        if self.action == 'retrieve':
            return serializers.EmployeGetSerializer
        
        if self.action == 'create':
            return serializers.EmployePostSerializer
        
        if self.action == 'update':
            return serializers.EmployeUpdateSerializer

        if self.action == 'destroy':
            return serializers.EmployeSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        temp_response_data = serializer.data.copy()
        temp_response_data.pop('password')
        return Response(temp_response_data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        self.save(serializer)

    def save(self, serializer, **kwargs):
        assert not hasattr(serializer, 'save_object'), (
            'Serializer `%s.%s` has old-style version 2 `.save_object()` '
            'that is no longer compatible with REST framework 3. '
            'Use the new-style `.create()` and `.update()` methods instead.' %
            (serializer.__class__.__module__, serializer.__class__.__name__)
        )

        assert hasattr(serializer, '_errors'), (
            'You must call `.is_valid()` before calling `.save()`.'
        )

        assert not serializer.errors, (
            'You cannot call `.save()` on a serializer with invalid data.'
        )

        # Guard against incorrect use of `serializer.save(commit=False)`
        assert 'commit' not in kwargs, (
            "'commit' is not a valid keyword argument to the 'save()' method. "
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
            "You can also pass additional keyword arguments to 'save()' if you "
            "need to set extra attributes on the saved model instance. "
            "For example: 'serializer.save(owner=request.user)'.'"
        )

        assert not hasattr(serializer, '_data'), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        validated_data = dict(
            list(serializer.validated_data.items()) +
            list(kwargs.items())
        )
        password = validated_data.pop('password')
        username = validated_data.get('username')
        user_details = {'username': username, 'password': password, 'email':None}
        user = user = User.objects.create_user(**user_details)

        validated_data['user'] = user

        if serializer.instance is not None:
            serializer.instance = serializer.update(serializer.instance, validated_data)
            assert serializer.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            serializer.instance = serializer.create(validated_data)
            assert serializer.instance is not None, (
                '`create()` did not return an object instance.'
            )
        serializer.instance.password = '**********'
        return serializer.instance
        
                     
