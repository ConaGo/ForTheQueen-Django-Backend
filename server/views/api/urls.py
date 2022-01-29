from django.urls import include
from django.urls import path

from server.views.api import index as api_index

urlpatterns = [path("", api_index.index)]
