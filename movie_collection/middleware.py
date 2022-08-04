import imp
from movie.models import Counter
from django.conf import settings

class CustomDebugMiddleware_first:
    def __init__(self, get_response):
        self.get_response = get_response
         
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        new_http_information = Counter(counter=response)
        new_http_information.save()

        # Code to be executed for each request/response after
        # the view is called.

        return response