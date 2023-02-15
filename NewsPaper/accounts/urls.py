from django.urls import path
from .views import UserUpdateView, upgrade_me, unsubscribe


urlpatterns = [
    path('account/', UserUpdateView.as_view(), name='personal_area'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('unsubscribe/', unsubscribe, name='unsubscribe'),
]
