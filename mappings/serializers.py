from rest_framework import serializers
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    validators = []

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id',
            'patient',
            'patient_name',
            'doctor',
            'doctor_name',
            'assigned_at'
        ]

    def validate(self, data):
        patient = data['patient']
        doctor = data['doctor']

        if PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor
        ).exists():
            raise serializers.ValidationError(
                {"message":"Doctor already assigned to this patient."}
            )

        return data