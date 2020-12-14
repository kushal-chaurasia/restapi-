from rest_framework import serializers
from .models import card


class CardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    card_no = serializers.IntegerField()
    expiry = serializers.DateField()
    cvv = serializers.IntegerField()

    class Meta:
        model = card
        fields = '__all__'

# def create(self, validate_data):
#     return card.objects.create(**validate_data)
