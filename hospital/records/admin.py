from django.contrib import admin
from records.models import PatientProfile,PatientRecords,MedCabinet
# Register your models here.


admin.site.register(PatientProfile)
admin.site.register(PatientRecords)
admin.site.register(MedCabinet)

