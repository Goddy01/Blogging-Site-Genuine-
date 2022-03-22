"""blog_project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog_app import views
from account.views import (
    registration_view, logout_view, 
    login_view, update_view  
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home_page, name='home_page'),
    re_path(r'^register/$', registration_view, name='register'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^login/update_profile/$', update_view, name='update'),


    path(
    "password_change/", views.PasswordChangeView.as_view(), name="password_change"
            ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
            ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
            ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
            ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
            ),
    ]
