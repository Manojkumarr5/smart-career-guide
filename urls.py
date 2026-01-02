from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    re_path(r'^(?P<template>[\w/-]+\.html)$', TemplateView.as_view(template_name='{{ template }}')),
]
