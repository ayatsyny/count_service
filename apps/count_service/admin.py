from django.contrib import admin
from .models import CountVisitSite


class VisitSiteAdmin(admin.ModelAdmin):
    model = CountVisitSite
    list_display = ['user', 'url_path']


admin.site.register(CountVisitSite, VisitSiteAdmin)
