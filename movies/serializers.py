from rest_framework import serializers
from movies.models import Movies
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):    
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self,obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate,2)

        return None