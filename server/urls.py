from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("server.views.urls")),
    path("api/", include("server.views.api.urls")),
]
