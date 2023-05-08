from rest_framework import serializers
from .models import Cars

class CarSerialize(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'name', 'model', 'm_no']