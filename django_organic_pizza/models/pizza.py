from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Pizza(models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    price = models.DecimalField( null=False, default=0.00, max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00') )] )
    pizza_type_id = models.ForeignKey("PizzaType", null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name) 
