from django.shortcuts import render

#Create your views here.
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse


#API defin
from .serializers import Task_CarbonSerializer

# model
from .models import Task_Carbon



@csrf_exempt
def tasks_carbon(request):
    '''
    List all task snippets
    '''

    if(request.method == 'GET'):

        # GET ALL HISTORY

        tasks_carbon = Task_Carbon.objects.all()

        task_carbonserializer = Task_CarbonSerializer(tasks_carbon, many=True)

        return JsonResponse(task_carbonserializer.data, safe=False)
    
    elif(request.method == 'POST'):

        data = JSONParser().parse(request)

        task_carbonserializer = Task_CarbonSerializer(data=data)

        if(task_carbonserializer.is_valid()):

            distance = data.get('distance')
            mpg = data.get('mpg')
            afec = data.get('afec')
            emission_factor = data.get('emission_factor', 8.89)

            fuel_consume = distance / mpg
            emissions = fuel_consume * emission_factor * afec

            #save result
            tasks_carbon = Task_Carbon.objects.create(
                distance=distance,
                mpg=mpg,
                afec=afec,
                emission_factor=emission_factor,
                result=emissions

            )

            task_carbonserializer = Task_CarbonSerializer(tasks_carbon)
            return JsonResponse(task_carbonserializer.data, status=201)
        
        return JsonResponse(task_carbonserializer.errors, status=400)


@csrf_exempt
def tasks_carbon_detail(request, pk):
    try:

        tasks_carbon = Task_Carbon.objects.get(pk=pk)
    
    except:

        return HttpResponse(status=404)

    
    if(request.method == 'DELETE'):

        tasks_carbon.delete()

        return HttpResponse(status=204)




