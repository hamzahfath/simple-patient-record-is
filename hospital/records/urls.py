from django.urls import path
from . import views


app_name = 'records'
urlpatterns = [
    path('',views.home,name='home'),
    path('createpatient/', views.PatientCreate.as_view(),name='create_patient'),
    path('patient/<int:pk>/',views.PatientDetail.as_view(),name='patient_detail'),
    path('patients/',views.PatientList.as_view(),name='patient_view'),

    path('createrecords/',views.PatientRecordsCreate.as_view(),name='create_record'),
    path('record/<int:pk>',views.PatientRecordsDetail.as_view(),name='record_detail'),

]