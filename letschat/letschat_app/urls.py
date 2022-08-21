# letschat_app/urls.py
from django.urls import path
from .views import app_index, room_name

app_name = 'letschat_app'
urlpatterns = [
    path('', app_index, name="index"),
    path('<str:name>/', room_name, name='room'),
]
