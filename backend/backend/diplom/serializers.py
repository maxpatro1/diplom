from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer()

    class Meta:
        model = Role
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dict_Group
        fields = '__all__'


# class ExecutorSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     group = GroupSerializer()
#
#     class Meta:
#         model = Executor
#         fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LabSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Course
        fields = '__all__'


