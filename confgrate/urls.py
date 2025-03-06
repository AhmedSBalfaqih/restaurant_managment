import os
from django.urls import path
from confgrate.views import RegisterView,UserDatatJson
from django.contrib.auth import views as auth_views

urlpatterns = [
# path('usersview', get_users.as_view(), name='usersview'),
path('UserDatatJson', UserDatatJson.as_view(), name='UserDatatJson'),
path('register/', RegisterView.as_view(), name='users-register'),

]