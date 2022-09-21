from rest_framework import generics, permissions

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
    permission_class = permissions.IsAuthenticatedOrReadOnly


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class UserGetView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.GET.get('username')
        return User.objects.filter(username=username)
