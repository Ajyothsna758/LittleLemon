from django.shortcuts import render

# Create your views here.
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def menuView(request):
    if request.method=="GET":
        items= MenuItem.objects.all()
        serialized_items= MenuItemSerializer(items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        serialized_item= MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)
    