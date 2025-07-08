from django.shortcuts import render
from rest_framework import generics
from . models import Menu, Booking
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Handles GET (list) and POST (create)
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Handles GET (retrieve), PUT (update), DELETE (destroy)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
