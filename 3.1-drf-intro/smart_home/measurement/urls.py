from django.urls import path

from measurement.views import ListCreateSensorView, RetrieveUpdateSensorView
from measurement.views import MeasurementView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListCreateSensorView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
