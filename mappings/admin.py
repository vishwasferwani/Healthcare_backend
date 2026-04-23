from django.contrib import admin
from .models import PatientDoctorMapping

# Register your models here.
@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'assigned_at')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('assigned_at',)
