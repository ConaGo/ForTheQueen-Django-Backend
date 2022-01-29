from django.http import HttpResponse


def index(request: HttpResponse):
    return HttpResponse("Welcome to For The Queen")
