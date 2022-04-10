from os import stat
import pickle

from django.contrib import messages
from django.shortcuts import redirect, render

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from api.serializers import ParameterSerializer
from api.models import Parameter

# Create your views here.

with open("./system.pickle", "rb") as f:
    system = pickle.load(f)

class ParameterListCreateView(APIView):

    def get(self, request, format=None):
        parameters = Parameter.objects.all()
        serializer = ParameterSerializer(parameters, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, format=None):
        parameters = request.data.get('parameters')
        parameters = parameters.split()
        parameter = Parameter.objects.create(
            voltage_r = str(round(float(parameters[0]), 4)),
            current_r = str(round(float(parameters[1]), 4)),
            voltage_y = str(round(float(parameters[2]), 4)),
            current_y = str(round(float(parameters[3]), 4)),
            voltage_b = str(round(float(parameters[4]), 4)),
            current_b = str(round(float(parameters[5]), 4))
        )
        serializer = ParameterSerializer(parameter)
        return Response(serializer.data, status=HTTP_200_OK)

class ParameterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class APIRoot(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'parameters': reverse('api:parameter-list-create', request=request),
            'toggle_system': reverse('api:toggle_system', request=request),
            'get_system_status': reverse('api:get_system_status', request=request),
        })


def index(request):
    if request.method == "GET":
        return render(request, 'api/index.html')
    
    else:
        ...

def home(request):
    if request.method == "GET":
        parameter = Parameter.objects.all().first()
        system_status = system["system_on"]
        return render(request, 'api/home.html', {'parameter': parameter, "system_status": system_status})


def toggle_system(request):
    global system
    system["system_on"] = not system["system_on"]
    with open("./system.pickle", "wb") as f:
        pickle.dump(system, f)
    return redirect("api:home")


class GetSystemStatus(APIView):
    def get(self, request, format=None):
        global system
        return Response({"system_status": "on" if system["system_on"] else "off"}, status=HTTP_200_OK)


def parameter_list(request):
    if request.method == "GET":
        parameters = Parameter.objects.all()[:100]
        return render(request, 'api/list.html', {'parameters': parameters})