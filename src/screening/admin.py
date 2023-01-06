from django.contrib import admin
from .models import Patient, Symptom, SymptomPatient, Diagnostic

# Register your models here.
admin.site.register(Patient)
admin.site.register(Symptom)
admin.site.register(SymptomPatient)
admin.site.register(Diagnostic)
