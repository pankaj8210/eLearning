# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.authentication.views import *

urlpatterns = [
    path('',index,name="index"),
    path('login/', login_view, name="login"),
    path('course-1/', course1, name="course1"),
    path('course-2/', course2, name="course2"),
    path('course-3/', course3, name="course3"),
    path('single-course/', coursed, name="coursed"),
    path('about/', about, name="about"),
    path('about2/', about2, name="about2"),
    path('instructor/',instructor,name="instructor"),
    path('instructorprofile/',instructorprofile,name="instructorprofile"),
    path('blog/', blog, name="blog"),
    path('blog2/', blog2, name="blog2"),
    
    path('confirmation/',confirmation, name="confirmation"),
    path('inquiry/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("inq/", stuinquiry, name="logout"),
    path("regg11/", reg11, name="logout"),
    path("ref/", Registerfill, name="logout"),
    path("rrh/", rrhomee, name="logout"),

]
