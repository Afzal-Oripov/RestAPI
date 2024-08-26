from django.urls import path
from .views import *


urlpatterns = [
    path('', UserApiView.as_view()),
    path('users/<int:pk>/', UserApiView.as_view(), name='user-detail'),  # Для PUT и DELETE
]
