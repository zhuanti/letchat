from django.shortcuts import render

# Create your views here.
# letschat_app/views.py
from django.shortcuts import render
def app_index(request):
   return render(request, 'letschat_app/index.html')


def room_name(request, name):
   return render(request, 'letschat_app/chatroom.html', {'room_name': name})