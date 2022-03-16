from rest_framework import generics, permissions

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
