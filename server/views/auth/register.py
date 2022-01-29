from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from server.serializers.register import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterSerializer
