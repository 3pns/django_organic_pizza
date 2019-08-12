import factory
from django_organic_pizza.models import Pizza, PizzaType
import random, decimal
from . import PizzaTypeFactory

class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    name = factory.Sequence(lambda n: 'pizza_{0}'.format(n))
    price = decimal.Decimal(random.randrange(0, 9999))/100
    pizza_type_id = PizzaTypeFactory.create()
