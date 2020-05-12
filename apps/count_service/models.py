from django.contrib.auth.models import User
from django.db import models


class CountVisitSite(models.Model):
    ip_address = models.GenericIPAddressField(db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    url_path = models.URLField(db_index=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'count visit site'
        verbose_name_plural = 'count visit sites'

    def __str__(self):
        return self.user.email
