import json

from rest_framework import generics, permissions
from ..labs.lab_1 import get_plot
from ..serializers import *


class LabListView(generics.ListAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class LabCreateView(generics.CreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class LabRetrieveView(generics.RetrieveAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class LabUpdateView(generics.UpdateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class LabsByCourseIdView(generics.ListAPIView):
    serializer_class = LabSerializer

    def get_queryset(self):
        course_id = self.request.GET.get('id')
        return Lab.objects.filter(course_id=course_id).order_by('id')


class CompletedLabsView(generics.ListAPIView):
    serializer_class = UserHasLabSerializer

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        return User_Has_Labs.objects.filter(user_id=user_id, is_compile=True)


def getLabFile(request):
    params = request.GET.get('params')
    json_object = json.loads(params)
    file = get_plot(params=json_object['params'])
    return file
