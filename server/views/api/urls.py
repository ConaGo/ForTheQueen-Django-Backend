from django.urls import include
from django.urls import path

from server.views.api import index as api_index
from server.views.api.savestates import SavestateViewset

urlpatterns = [path("savestates/", SavestateViewset.as_view({"get": "list"}))]
