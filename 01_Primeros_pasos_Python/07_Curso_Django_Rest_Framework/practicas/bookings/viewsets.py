from rest_framework import viewsets

from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Bookings


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Bookings.objects.all()