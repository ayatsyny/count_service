from django.conf import settings
from .log import Logger
from .models import CountVisitSite


class IPAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def __call__(self, request):
        remoteip = self.get_client_ip(request)

        if request.user.is_authenticated:
            if not CountVisitSite.objects.filter(user_id=request.user.pk, url_path=request.path).exists():
                CountVisitSite.objects.create(ip_address=remoteip, user=request.user, url_path=request.path)
                if settings.DEBUG:
                    logger = Logger(settings.LOG_FILE_NAME)
                    logger.info('visited user_email: {} url_path: {} ip: {}'.format(request.user.email, request.path, remoteip))
        response = self.get_response(request)
        return response
