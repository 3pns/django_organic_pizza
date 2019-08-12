from django.test import TestCase
from tests.factories import *
from expects import *
from django_organic_pizza.models import *

from django.db import IntegrityError
from django.core.exceptions import ValidationError

class PizzaModelTest(TestCase):
    def setUp(self):
        self.pizza = PizzaFactory.create()

    def test_property_name(self):
        expect(self.pizza).to(have_property('name'))

    def test_property_price(self):
        expect(self.pizza).to(have_property('price'))

    def test_property_pizza_type_id(self):
        expect(self.pizza).to(have_property('pizza_type_id'))

    def test_unicity_of_name(self):
        duplicate_pizza = PizzaFactory.build(name = self.pizza.name)
        expect(duplicate_pizza.save).to(raise_error(IntegrityError))

    def test_negative_price(self):
        pizza = PizzaFactory.build(price = -42.42)
        with self.assertRaises(ValidationError):
            expect(pizza.full_clean()).to(raise_error(ValidationError))

    def test_to_string(self):
        expect("{}".format(self.pizza)).to(equal(self.pizza.name))

    def test_buy(self):
        transaction = self.pizza.buy()
        expect(transaction).to(be_a(Transaction))
        expect(transaction.pizza_id).to(equal(self.pizza.id))
        expect(transaction.price).to(equal(self.pizza.price))
