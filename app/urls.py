from django.urls import path
from .views import getRoutes, getFractionPrices, add_price


urlpatterns = [
    path('', getRoutes),
    path('prices/', getFractionPrices),
    path('prices/add/', add_price),
]
