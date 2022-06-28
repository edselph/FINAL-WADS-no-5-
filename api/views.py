from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request): 
    drinkz = {
        'name':'Coffee', 'price':13
    }
    return Response(drinkz)
