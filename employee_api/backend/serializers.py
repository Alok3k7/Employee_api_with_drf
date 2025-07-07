from rest_framework import serializers
from .models import City, Employee


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'salary', 'city', 'is_active']
