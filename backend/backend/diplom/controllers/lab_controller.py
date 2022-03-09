from rest_framework import generics

from ..serializers import *


class LabListView(generics.ListAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class LabCreateView(generics.CreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class LabRetrieveView(generics.RetrieveAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class LabUpdateView(generics.UpdateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
