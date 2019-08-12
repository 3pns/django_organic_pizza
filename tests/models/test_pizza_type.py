from django.test import TestCase
from tests.factories import *
from expects import *
from django.db import IntegrityError

class PizzaTypeModelTest(TestCase): #(TransactionTestCase):
    def setUp(self):
        self.pizza_type = PizzaTypeFactory.create()

    def test_property_name(self):
        expect(self.pizza_type).to(have_property('name'))

    def test_unicity_of_name(self):
        duplicate_pizza_type = PizzaTypeFactory.build(name = self.pizza_type.name)
        expect(duplicate_pizza_type.save).to(raise_error(IntegrityError))
