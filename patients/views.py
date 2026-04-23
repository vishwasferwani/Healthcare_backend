from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(owner=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.owner != request.user:
            return Response(
                {"error": "You do not have permission to delete this patient."},
                status=status.HTTP_403_FORBIDDEN
            )

        self.perform_destroy(instance)

        return Response(
            {"message": "Patient deleted successfully."},
            status=status.HTTP_200_OK
        )