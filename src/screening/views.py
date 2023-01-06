import datetime

from django.shortcuts import render, redirect
from django.views import View

from .models import Patient, Symptom, SymptomPatient, Diagnostic


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            registered_patients = Patient.objects.filter(was_attended=False, is_active=True).order_by('active_date')

            attended_patients = Patient.objects.filter(was_attended=True, is_active=True).order_by('-priority')

            context = {'registered_patients': registered_patients, 'attended_patients': attended_patients}
            return render(request, 'screening/index.html', context)
        return redirect('login')


class CreatePatientView(View):
    def get(self, request):
        return render(request, 'screening/create-patient.html')

    def post(self, request):
        if request.user.is_authenticated:
            name = request.POST['patient_name']
            age = request.POST['patient_age']
            cpf = request.POST['patient_cpf']
            address = request.POST['patient_address']
            phone = request.POST['patient_phone']

            Patient.objects.create(
                name=name,
                age=int(age),
                cpf=cpf,
                address=address,
                phone=phone
            )

            return redirect('index')
        return redirect('login')


class AddExistentPatient(View):
    def get(self, request):
        patient_list = Patient.objects.filter(is_active=False).order_by('name')
        context = {'patient_list': patient_list}
        return render(request, 'screening/add-existent-patient.html', context)

    def post(self, request):
        pk = int(request.POST['patient'])
        patient = Patient.objects.get(pk=pk)
        patient.active_date = datetime.datetime.now()
        patient.is_active = True
        patient.save()

        return redirect('index')


class CreateSymptom(View):
    def post(self, request, pk):
        name = request.POST['name'].upper()
        priority = int(request.POST['priority'])

        Symptom.objects.create(name=name, priority=priority)
        return redirect('register-symptoms', pk)


class RegisterSymptomsView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            patient = Patient.objects.get(pk=pk)
            symptoms = Symptom.objects.all().order_by('name')
            context = {'patient': patient, 'symptoms': symptoms}
            return render(request, 'screening/register-symptoms.html', context)
        return redirect('login')

    def post(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        RegisterSymptomsView.create_all_symptoms_patients_relations(request, patient)

        patient.was_attended = True
        patient.define_patient_priority()
        patient.save()

        return redirect('index')

    @classmethod
    def create_all_symptoms_patients_relations(cls, request, patient):
        for name, pk in request.POST.items():
            if name != 'csrfmiddlewaretoken':
                symptom = Symptom.objects.get(pk=pk)
                SymptomPatient.objects.create(symptom=symptom, patient=patient)


class GenerateDiagnosticView(View):
    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        symptoms = patient.get_symptoms()

        context = {'patient': patient, 'symptoms': symptoms}
        return render(request, 'screening/generate-diagnostic.html', context)

    def post(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        comorbidity = request.POST['comorbidity']
        prescription = request.POST['prescription']

        Diagnostic.objects.create(
            patient=patient,
            comorbidity=comorbidity,
            prescription=prescription
        )
        patient.free_patient()

        return redirect('index')


class UnsafeView(View):
    template_name = 'screening/unsafe.html'
    def get(self, request):
        return render(request, self.template_name)