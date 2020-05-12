from django import template
from django.template.defaultfilters import stringfilter
from apps.count_service.models import CountVisitSite

register = template.Library()


@register.filter
@stringfilter
def page_count(value):
    return CountVisitSite.objects.filter(url_path=value.lower().strip()).count()
