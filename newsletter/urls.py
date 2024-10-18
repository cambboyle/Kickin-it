from django.urls import path
from .views import subscribe, unsubscribe, unsubscribe_confirmation

urlpatterns = [
    path('subscribe/', subscribe, name='newsletter_subscribe'),
    path(
        'unsubscribe/<str:email>/',
        unsubscribe,
        name='newsletter_unsubscribe'
        ),
    path(
        'unsubscribe/confirmation/',
        unsubscribe_confirmation,
        name='newsletter_unsubscribe_confirmation'
        ),
]
