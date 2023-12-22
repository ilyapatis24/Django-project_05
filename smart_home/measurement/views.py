from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorUpdateSerializer

class GetSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Measurement(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateData(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer
    
    
class GetSensorInstance(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    

    