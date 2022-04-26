# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps.authentication.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(user)
admin.site.register(StudentInquiry)
