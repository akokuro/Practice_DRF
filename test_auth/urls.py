from django.urls import re_path, include  
from .views import RegistrationAPIView
from .views import LoginAPIView, HelloApiView

urlpatterns = [
    re_path(r'^signup/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^hello/?$', HelloApiView.as_view(), name='user_hello'),
]