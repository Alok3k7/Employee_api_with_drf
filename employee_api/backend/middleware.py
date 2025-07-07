import uuid
import threading

_thread_locals = threading.local()


def get_request_id():
    return getattr(_thread_locals, 'request_id', None)


class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request_id = str(uuid.uuid4())
        response = self.get_response(request)
        return response
