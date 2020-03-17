"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import re_path, path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name="post_list"),
    path('blog/', include('blog.urls')),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),
    path('', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('like/', views.like_post, name="like_post"),     
    #This path will request the customer to type in the email address he or she wants to receive the new instructions to reset the password
    path('password-reset/',
        authViews.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
 
    #This will inform the customer a new email has been sent with the instruction
    path('password-reset/done/',
         authViews.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
 
    #This path will provide a specific url with a base64 hash as well as with a token
    path('password-reset-confirm/<uidb64>/<token>/',
        authViews.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
 
    #This will inform the customer that the password has been changed
    path('password-reset-complete/',
        authViews.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
        ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
