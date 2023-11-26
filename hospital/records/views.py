from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import PatientProfile,PatientRecords,MedCabinet
from django.db.models import F

# Create your views here.

def home(request):
    return render(request, 'records/home.html')

#PATIENT IDs
class PatientCreate(CreateView): #book_form.html
    model =  PatientProfile
    fields = '__all__'

class PatientDetail(DetailView):
    model = PatientProfile

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the patient records
        # context['patient_records'] = PatientRecords.objects.filter(patient_name=self.object)
        # for item in context['patient_records'].all():
        #     print(item.prescription)

        patient_records = PatientRecords.objects.filter(patient_name=self.object)
        for record in patient_records:
            record.prescriptions = record.prescription.all()
            #print(record.prescription)
        context['patient_records'] = patient_records
        print(context['patient_records'])
        return context

class PatientList(ListView):
    model=PatientProfile

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the patient records
        context['patients'] = PatientProfile.objects.all()
        return context

#PATIENT RECORDS 
class PatientRecordsCreate(CreateView): #patientrecords_form.html
    model =  PatientRecords
    fields = '__all__'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)

        # Get the prescription from the form data
        prescriptions = form.cleaned_data.get('prescription')
        # Returning multiple querryset, each of them reffering to medicine instances:
        # <QuerySet [<MedCabinet: Paracetamol stock: 498>]>
        # <QuerySet [<MedCabinet: Thrombopop stock: 249>]>
        # <QuerySet [<MedCabinet: metaheuristik stock: 199>]>

        for prescription in prescriptions:
        # Decrease the stock of the prescribed medicine
            #print(MedCabinet.objects.filter(pk=prescription.pk))
            MedCabinet.objects.filter(pk=prescription.pk).update(stock=F('stock') - 1)  
            
            #for each queryset, it will matching the pk of the Medicine models with the querried from prescription 

        return response


class PatientRecordsDetail(DetailView):
    model = PatientRecords

#MEDICINE 
