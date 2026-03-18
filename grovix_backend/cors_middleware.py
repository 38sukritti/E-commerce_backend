"""
Custom CORS middleware that adds Access-Control-Allow-Origin headers
to every single response. This is a fallback because django-cors-headers
was not adding headers reliably on Render.
"""


class CorsMiddleware:
    """Add CORS headers to all responses."""

    ALLOWED_ORIGIN = 'https://grovixstudio-dusky.vercel.app'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Handle preflight OPTIONS requests
        if request.method == 'OPTIONS':
            from django.http import HttpResponse
            response = HttpResponse()
            response.status_code = 200
        else:
            response = self.get_response(request)

        response['Access-Control-Allow-Origin'] = self.ALLOWED_ORIGIN
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Accept, Accept-Encoding, Authorization, Content-Type, DNT, Origin, User-Agent, X-CSRFToken, X-Requested-With'
        response['Access-Control-Max-Age'] = '86400'
        return response
