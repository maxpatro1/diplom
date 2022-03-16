from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
