from rest_framework import generics, permissions

from ..serializers import *


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CourseRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly
