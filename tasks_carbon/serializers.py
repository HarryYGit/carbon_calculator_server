from rest_framework import routers,serializers,viewsets
from .models import Task_Carbon

class Task_CarbonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task_Carbon
        fields = ['id', 'distance', 'mpg', 'afec', 'emission_factor', 'result', 'created_at']
        