from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Parameter


class ParameterSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:parameter-detail')
    power_r = serializers.CharField(read_only=True)
    power_y = serializers.CharField(read_only=True)
    power_b = serializers.CharField(read_only=True)

    class Meta:
        model = Parameter
        exclude = ('created', 'updated')