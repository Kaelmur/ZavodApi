from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_price(request):
    serializer = PriceSerializer(data=request.data)

    if serializer.is_valid():
        fraction = serializer.validated_data['fraction']
        price = serializer.validated_data['price']
        existing_fraction_price = FractionPrice.objects.filter(fraction=fraction).first()
        if existing_fraction_price:
            existing_fraction_price.price = price
            existing_fraction_price.save()
            return Response({'message': 'Цена на фракцию обновлена'}, status=status.HTTP_200_OK)
        else:
            serializer.save()
            return Response({'message': 'Цена на фракцию установлена'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
