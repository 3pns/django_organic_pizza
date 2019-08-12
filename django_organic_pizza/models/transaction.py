from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Transaction(models.Model):
    price = models.DecimalField( null=False, default=0.00, max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00') )] )
    pizza = models.ForeignKey("Pizza", null=False, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return "{}".format(self.price) 
