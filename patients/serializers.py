from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Patient
        fields = '__all__'

    def validate_age(self, value):
        if value <= 0 or value > 120:
            raise serializers.ValidationError("Enter valid age.")
        return value