from django.urls import path
from . import views

urlpatterns = [
    path('subscribe_newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
]