from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment
from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsDoctor



class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_clases = [IsAuthenticated]

    @action(['POST'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor está en vacaciones"})

    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor NO está en vacaciones"})
    

    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()

        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        
        
    # Nuevo endpoint para eliminar una cita
    @action(detail=True, methods=['delete'], url_path='delete-appointment/(?P<appointment_id>[^/.]+)')
    def delete_appointment(self, request, pk=None, appointment_id=None):
        doctor = self.get_object()  # Obtener el doctor por su ID
        try:
            # Intentamos obtener la cita para ese doctor y con el ID proporcionado
            appointment = Appointment.objects.get(id=appointment_id, doctor=doctor)
            appointment.delete()  # Eliminar la cita
            return Response({"status": "Cita eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({"error": "Cita no encontrada."}, status=status.HTTP_404_NOT_FOUND)