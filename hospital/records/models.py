from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.



class PatientProfile(models.Model):
    BLOODTYPE_CHOICES = [
    ("A", "A"),
    ("AB", "AB"),
    ("B", "B"),
    ("O", "O"),
    ('-','None'),
]
    patient_name = models.CharField(max_length=100)
    patient_address = models.TextField(max_length=300)
    Patient_bloodtype = models.CharField(choices=BLOODTYPE_CHOICES,max_length=10)
    patient_age = models.IntegerField(default=0)
    patient_comorbid = models.TextField(default='No Comorbid')
    patient_note = models.TextField(default='None')
    patient_apply = models.DateTimeField(auto_created=True,auto_now=True)
    patient_systol = models.IntegerField(default=120)
    patient_diastol = models.IntegerField(default=80)

    class Meta:
        ordering = ['patient_name']
    def __str__(self) -> str:
        return f"{self.patient_name}"
    
    def get_absolute_url(self):
        return reverse("patient_detail", kwargs={"pk": self.pk})

class PatientRecords(models.Model):
    timestamp = models.DateTimeField(auto_created=True,auto_now=True)
    patient_name = models.ForeignKey(PatientProfile,on_delete=models.SET_NULL,blank=True,null=True)
    diagnose = models.TextField(max_length=300)
    prescription = models.ManyToManyField('MedCabinet')
    notes = models.TextField(max_length=300)
    follow_up = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self) -> str:
        return f"Records {self.patient_name} on {self.timestamp}"
    
    def get_absolute_url(self):
        return reverse("records:record_detail", kwargs={"pk": self.pk})



class MedCabinet(models.Model):
    medicine_name = models.CharField(max_length=200)
    dose = models.TextField(max_length=10)
    description = models.TextField(max_length=300)
    stock = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.medicine_name} stock: {self.stock}"
    