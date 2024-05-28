from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from .serializers import PriceSerializer
from .models import FractionPrice


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/fraction_prices'},
        {'POST': '/api/fraction_prices'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'}
    ]

    return Response(routes)


@api_view(['GET'])
def getFractionPrices(request):
    fraction_prices = FractionPrice.objects.all()
    serializer = PriceSerializer(fraction_prices, many=True)
    return Response(serializer.data)
