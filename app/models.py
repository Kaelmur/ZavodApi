from django.db import models
from django.utils import timezone


class FractionPrice(models.Model):
    fraction = models.CharField(max_length=100, choices=[
        ("0-5", "0-5"), ("5-20", "5-20"), ("20-40", "20-40"),
        ("5-40", "5-40"), ("40-70", "40-70"),
        ('Rubble stone', "Бутовый камень")
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
