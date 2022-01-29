import functools

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.utils.decorators import method_decorator


def internal_or_403(view_func):
    """
    A view decorator which returns the provided view function,
    modified to return a 403 when the remote address is not in
    the list of internal IPs defined in settings.
    """

    @functools.wraps(view_func)
    def wrapper(request: HttpRequest, *args, **kwargs):
        if not request.META["REMOTE_ADDR"] in settings.INTERNAL_IPS:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapper


class Internal(object):
    """
    A mix-in for class based views, which disallows requests from
    non-internal IPs.
    """

    @method_decorator(internal_or_403)
    def dispatch(self, *args, **kwargs):
        return super(Internal, self).dispatch(*args, **kwargs)
