from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/chart/<str:plant_id>', views.ChartData.as_view(), name='api-chart'),
    path('api/plant-data', views.PlantData.as_view(), name='plant-data'),
    path('api/upload-csv', views.UploadCSV.as_view(), name='upload-csv')
]
