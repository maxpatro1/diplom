from rest_framework import generics

from ..serializers import *

CONST_STUDENT_ROLE = 1


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     queryset = queryset.filter(role=CONST_STUDENT_ROLE)
    #     return queryset


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
