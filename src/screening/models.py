from django.db import models
from datetime import datetime


class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    cpf = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    was_attended = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=datetime.now)
    active_date = models.DateTimeField(default=datetime.now)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def define_patient_priority(self):
        symptoms = self.get_symptoms()

        for symptom in symptoms:
            if self.priority < symptom.priority:
                self.priority = symptom.priority

    def free_patient(self):
        self.is_active = False
        self.was_attended = False
        self.priority = 0

        symptoms_patient = SymptomPatient.objects.filter(patient=self)
        for relation in symptoms_patient:
            relation.delete()

        self.save()

    def get_symptoms(self):
        symptoms = []
        symptoms_patient = SymptomPatient.objects.filter(patient=self)
        for relation in symptoms_patient:
            symptoms.append(relation.symptom)

        return symptoms


class Symptom(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name}'


class SymptomPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient} -> {self.symptom}'


class Diagnostic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comorbidity = models.CharField(max_length=50)
    prescription = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.comorbidity}'
