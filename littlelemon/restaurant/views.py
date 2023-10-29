from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import MenuSerializer, UserSerializer, BookingSerializer

# Create your views here.
class MenuItemView(generics.ListCreateView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['title']
    ordering_fields = ['price', 'inventory']

    def get_queryset(self):
        return Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

class BookingViewSet(viewsets.ModelViewSet):
    def list(self, request):
        all_bookings = Booking.objects.all()
        items = BookingSerializer(all_bookings, many=True)
        permission_classes = [permissions.IsAuthenticated]
        return Response(items.data)