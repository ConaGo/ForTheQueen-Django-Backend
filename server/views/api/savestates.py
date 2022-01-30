from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from server.models import Savestate
from server.serializers.savestate import SavestateSerializer


class SavestateViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Savestate.objects
        else:
            return user.profile.savestate_set

    def list(self, request):
        serializer = SavestateSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


# @api_view(["GET"])
# def view(request: Request):
#     return Response({"message": "Hola"})
