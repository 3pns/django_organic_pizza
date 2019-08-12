from django.core.management.base import BaseCommand, CommandError
from django_organic_pizza.models import *
import random, decimal

class Command(BaseCommand):
    help = 'Lots of free tasty pizza just for you'

    def handle(self, *args, **options):
        # generate pizza types
        pizza_types = []
        pizza_types.append(PizzaType.objects.get_or_create(name="California")[0])
        pizza_types.append(PizzaType.objects.get_or_create(name="Chicago")[0])
        pizza_types.append(PizzaType.objects.get_or_create(name="New York")[0])

        # get existing current pizzas in the database
        keywords = ["Margherita", "Marinara", "Quattro", "Stagioni", "Carbonara", "Frutti", "di Mare", "Formaggi", "Crudo", "Napoletana", "Pugliese", "Montanara", "Emiliana", "Romana", "Fattoria"]
        pizzas = []
        for pizza_type in pizza_types:
            number_of_pizzas = random.randint(10,30)
            for _ in range(number_of_pizzas):
                index_1 = random.randint(0,len(keywords)-1)
                index_2 = random.randint(0,len(keywords)-1)
                
                random_name = "{0} {1} {2}".format(pizza_type.name, keywords[index_1], keywords[index_2])
                pizza = Pizza.objects.get_or_create(name=random_name, pizza_type=pizza_type)[0]
                pizza.price = decimal.Decimal(random.randrange(0, 9999))/100
                pizza.save()
                pizzas.append(pizza)
        for pizza in pizzas:
            buy_count = random.randint(0,100)
            for _ in range(buy_count):
                pizza.buy()
