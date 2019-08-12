import factory
from django_organic_pizza.models import Transaction, Pizza
import random, decimal
from . import PizzaFactory

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    price = decimal.Decimal(random.randrange(0, 9999))/100
    pizza_id = PizzaFactory.create()
