from rest_framework import serializers
from .models import GiphyCalendar

class GiphySerializer(serializers.ModelSerializer):
    class Meta:
        model = GiphyCalendar
        fields = ('date', 'url', 'description')