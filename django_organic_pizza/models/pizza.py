from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from .transaction import Transaction

class Pizza(models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    price = models.DecimalField( null=False, default=0.00, max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00') )] )
    pizza_type = models.ForeignKey("PizzaType", null=False, on_delete=models.CASCADE)

    def buy(self):
        return Transaction.objects.create(pizza = self, price = self.price)
