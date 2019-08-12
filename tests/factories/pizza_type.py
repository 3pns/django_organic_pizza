import factory
from django_organic_pizza.models import PizzaType

class PizzaTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PizzaType

    name = factory.Sequence(lambda n: 'pizza_type_{0}'.format(n))
