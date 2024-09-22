from rest_framework import serializers
from .models import identif

class identifSerializer(serializers.ModelSerializer):
    class Meta:
        model = identif
        fields = ('id', 'appID', 'userID', 'created','toTestID', 'tipoID', 'file', 'result')
        read_only_fields = ('created','result',)
    
        
        