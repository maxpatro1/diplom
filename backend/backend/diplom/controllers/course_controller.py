from rest_framework import generics, permissions

from ..serializers import *


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class StartedCoursesView(generics.ListAPIView):
    serializer_class = UserHasCourseSerializer

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        return User_Has_Courses.objects.filter(user_id=user_id)


class CourseRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly
