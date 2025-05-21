from .serializers import PatientSerializer
from .models import Patient

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,  DestroyAPIView, RetrieveUpdateDestroyAPIView  

class ListPatientsView(ListAPIView, CreateAPIView):
    allowe_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowe_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()