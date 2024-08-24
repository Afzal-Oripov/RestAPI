from django.urls import path
from .views import *


urlpatterns = [
    path('', UserApiView.as_view()),
]