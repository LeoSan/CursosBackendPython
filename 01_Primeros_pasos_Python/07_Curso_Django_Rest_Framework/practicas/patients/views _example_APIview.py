from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView  

from .serializers import PatientSerializer
from .models import Patient

class ListPatientsView(APIView):
    allowe_methods = ["GET", "POST"]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)  # Deserializar los datos enviados por el cliente
        if serializer.is_valid(raise_exception=True):  # Verificar si los datos son válidos
            serializer.save()  # Guardar el nuevo paciente en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolver los datos del paciente creado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si hay errores, devolverlos

class DetailPatientsView(APIView):
    allowe_methods = ["GET", "PUT", "DELETE"]

    def get(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)  # Devolver los datos del paciente creado
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)  # Si hay errores, devolverlos

    def put(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
            serializer = PatientSerializer(patient, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()  # Guardar el paciente en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolver los datos del paciente editados
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)  # Si hay errores, devolverlos
    
    def delete(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
            patient.delete()
            return Response(status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)  # Si hay errores, devolverlos
