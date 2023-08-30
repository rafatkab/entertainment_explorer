from rest_framework import serializers
from account_management.models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
class MovieRatingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatingsList
        fields = '__all__'