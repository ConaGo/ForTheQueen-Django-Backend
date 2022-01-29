from django.urls import include
from django.urls import path

from server.views import index

urlpatterns = [path("", index.index, name="index")]
