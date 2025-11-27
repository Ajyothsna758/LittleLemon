from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import UserSerializer, MenuSerializer, Bookingserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def hello(request):
    return HttpResponse("<h2>Hi Customer</h2>")

# api User
#functional view
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def userView(request):
    if request.method=="GET":
        users= User.objects.all()
        serialized_users= UserSerializer(users, many=True)
        return Response(serialized_users.data)
    if request.method=="POST":
        serialized_user= UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data)   

# generics
class UserGenericView(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer   
    permission_classes=[IsAuthenticated]  

# viewsets 
class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[TokenAuthentication, SessionAuthentication]
    permission_classes=[IsAuthenticated]

# Menu API
#using generic views
class MenuItemView(generics.ListCreateAPIView):
    queryset= Menu.objects.all()
    serializer_class=MenuSerializer  
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer   

# Booking API
# using viewset 
class BookingView(viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class=Bookingserializer
    permission_classes=[IsAuthenticated]
            
         
  
