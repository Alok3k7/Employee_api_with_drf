from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError

from .models import Employee, City
from .serializers import EmployeeSerializer, CitySerializer
from rest_framework import serializers
from django.shortcuts import render
import logging




logger = logging.getLogger('backend')


def some_view(request):
    logger.info("Employee created successfully")


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    try:
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=201)
    except IntegrityError:
        return Response({'error': 'Username already exists'}, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response({'status': 'Logged out successfully'})
    except Exception:
        return Response({'error': 'Logout failed'}, status=400)


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'department', 'city__name']

    def get_queryset(self):
        return Employee.objects.filter(is_active=True)

    def perform_create(self, serializer):
        city_id = self.request.data.get('city')
        try:
            city = City.objects.get(id=city_id)
        except City.DoesNotExist:
            raise serializers.ValidationError("Invalid city ID")
        serializer.save(city=city)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def employee_detail(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            city_id = request.data.get('city')
            try:
                city = City.objects.get(id=city_id)
            except City.DoesNotExist:
                return Response({'error': 'City not found'}, status=404)

            emp.name = serializer.validated_data['name']
            emp.email = serializer.validated_data['email']
            emp.department = serializer.validated_data['department']
            emp.salary = serializer.validated_data['salary']
            emp.city = city
            emp.save()
            return Response(EmployeeSerializer(emp).data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=204)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def deactivate_employee(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    emp.is_active = False
    emp.save()
    return Response({'status': 'Employee deactivated'})


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def activate_employee(request, pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    emp.is_active = True
    emp.save()
    return Response({'status': 'Employee activated'})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def frontend(request):
    return render(request, "frontend.html")