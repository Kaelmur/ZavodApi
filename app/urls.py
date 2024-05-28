from django.urls import path
from .views import getRoutes, getFractionPrices


urlpatterns = [
    path('', getRoutes),
    path('prices/', getFractionPrices),
]
