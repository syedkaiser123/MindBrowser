from rest_framework import serializers
from management.models import Manager, Employee
from django.contrib.auth.models import User
import re
from datetime import datetime


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployePostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        help_text="""
        Should have at least one number.
        Should have at least one uppercase and one lowercase character.
        Should have at least one special symbol.
        Should be between 6 to 20 characters long.
        """,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = Employee
        fields = ['username','first_name', 'last_name', 'address', 'dob', 'company', 'password', 'mobile', 'city']

        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).count():
            raise serializers.ValidationError('Username already used. please try another username')
        return value

    def validate_passowrd(self, value):
        error_message = """
        Should have at least one number.
        Should have at least one uppercase and one lowercase character.
        Should have at least one special symbol.
        Should be between 6 to 20 characters long.
        """
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pattern = re.compile(reg)
        match = re.search(pattern, value)

        if not match:
            raise serializers.ValidationError(error_message)
        return value
    
    def validate_mobile(self, value):
        if len(value) != 10:
            raise serializers.ValidationError('Please enter a valid Mobile No.')
        return value

    def validate_dob(self, value):
        import ipdb; ipdb.set_trace()
        if datetime.today().date()<value:
            raise serializers.ValidationError('Enter a valid DOB')

class EmployeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
