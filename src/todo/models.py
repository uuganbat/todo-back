# -*- coding:utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE
    )
    name = models.TextField(_("Name"))
    date = models.DateTimeField(_("Date"), auto_now_add=True)
    complete = models.BooleanField(_("Complete"), default=False)

    def __str__(self):
        return self.name
