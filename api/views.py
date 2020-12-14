from .serializers import CardSerializer
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import card

# Create your views here.


@csrf_exempt
def card_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = CardSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Transaction Succesful'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


def card_detail(request, ck):
    Card = card.objects.get(id=ck)
    serializer = CardSerializer(Card)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
