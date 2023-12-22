from django.urls import path

from measurement.views import GetSensors, Measurement, GetSensorInstance, UpdateData

urlpatterns = [
    path("sensors/update/<pk>/", UpdateData.as_view()),
    path("sensors/", GetSensors.as_view()),
    path("sensors/<pk>/", GetSensorInstance.as_view()),
    path("measurements/", Measurement().as_view()),
]
