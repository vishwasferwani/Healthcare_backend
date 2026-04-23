from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import MappingSerializer

# Create your views here.
class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    #no put patch for this viewset, only get post delete
    http_method_names = ['get', 'post', 'delete', 'head', 'options']

    queryset = PatientDoctorMapping.objects.all().order_by('-assigned_at')
    """all doctors for a patient"""
    def retrieve(self, request, *args, **kwargs):
        patient_id = kwargs.get('pk')
        queryset = PatientDoctorMapping.objects.filter(
            patient_id=patient_id
        ).order_by('-assigned_at')
        if not queryset.exists():
            return Response(
                {"message": "No doctors assigned to this patient."},
                status=status.HTTP_200_OK
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Doctor removed from patient successfully."}, status=status.HTTP_200_OK)