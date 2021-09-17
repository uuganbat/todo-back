# -*- coding:utf-8 -*-

from django.urls import path

from . import views as v

app_name = "ui"
urlpatterns = [
    path("", v.home, name="home"),
]
