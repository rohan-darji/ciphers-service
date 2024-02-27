from django.urls import path
from .views import encode, greetings

urlpatterns = [
    path('', greetings),
    path('caesar/<str:plaintext>/<int:shift>', encode),
]