from ddf import G
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase

from server.middleware.server_auth import ServerAuthMiddleware


class TestAuth(TestCase):
    def test_something(self):
        user = G(User, password="test")
        c = Client()
        request = c.post("/login/", username=User).request
        middleware = ServerAuthMiddleware(lambda: True)
        response = middleware.process_request(request)
        print(response)
        self.assertTrue(False)
