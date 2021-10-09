import pandas as pd

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SolarPlant
from .serializers import PlantSerializer


# Create your views here.

class UploadCSV(APIView):
    def post(self, request):
        file = request.data['file']
        data = pd.read_csv(file)
        print(data.head())

        plants = [
            SolarPlant(
                plant_id=data.iloc[row]['plant_id'],
                date=data.iloc[row]['date'],
                parameter=data.iloc[row]['parameter'],
                value=data.iloc[row]['value']
            )
            for row in range(len(data))
        ]

        SolarPlant.objects.bulk_create(plants)
        return Response(data={'message': 'The file has been succesfully loaded'}, status=status.HTTP_200_OK)


def index(request):
    '''
    For homepage
    '''
    plant_ids = SolarPlant.objects.values_list(
        'plant_id', flat=True).distinct().order_by('plant_id')
    context = {
        'plant_ids': plant_ids
    }
    print(context['plant_ids'])
    return render(request, 'solar_chart/index.html', context)


class ChartData(APIView):
    '''
    To generate data points for graph
    '''

    def get(self, request, plant_id):
        generation_points = [{'x': data.date,
                              'y': data.value}
                             for data in SolarPlant.objects.filter(plant_id=plant_id, parameter='generation').order_by('date')]
        irradiation_points = [{'x': data.date,
                               'y': data.value}
                              for data in SolarPlant.objects.filter(plant_id=plant_id, parameter='irradiation').order_by('date')]

        data = {
            'generation_points': generation_points,
            'irradiation_points': irradiation_points,
        }
        return Response(data)


class PlantData(APIView):
    plant_serializer = PlantSerializer

    def get_object(self, plant_id=None, parameter=None, from_date=None, to_date=None):
        print(parameter)
        if plant_id:
            return SolarPlant.objects.filter(plant_id=plant_id)
        if parameter:
            return SolarPlant.objects.filter(parameter=parameter)
        if from_date and to_date:
            return SolarPlant.objects.filter(date__gte=from_date) & SolarPlant.objects.filter(date__lt=to_date)
        if plant_id and parameter:
            return SolarPlant.objects.filter(plant_id=plant_id, parameter=parameter)

    def get(self, request):
        plant_id = request.GET.get('plant_id', None)
        parameter = request.GET.get('parameter', None)
        from_date = request.GET.get('from_date', None)
        to_date = request.GET.get('to_date', None)

        print(parameter)
        if plant_id:
            object = self.get_object(plant_id)
        if parameter:
            object = self.get_object(parameter=parameter)
        if from_date and to_date:
            object = self.get_object(from_date=from_date, to_date=to_date)

        print(object)
        if object:
            serializer = self.plant_serializer(instance=object, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Please enter a param'}, status=status.HTTP_400_BAD_REQUEST)
