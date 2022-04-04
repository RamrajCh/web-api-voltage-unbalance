from django.contrib import messages
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django.views.generic import ListView

from api.serializers import ParameterSerializer
from api.models import Parameter

# Create your views here.


class ParameterListCreateView(ListCreateAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class ParameterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class APIRoot(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'parameters': reverse('api:parameter-list-create', request=request),
        })


def index(request):
    if request.method == "GET":
        return render(request, 'api/index.html')
    
    else:
        ...

def home(request):
    if request.method == "GET":
        parameter = Parameter.objects.all().first()
        return render(request, 'api/home.html', {'parameter': parameter, "active":"home"})