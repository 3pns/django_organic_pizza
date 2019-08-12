from django.test import TestCase
from tests.factories import *
from expects import *
from django.db import IntegrityError
from django.core.exceptions import ValidationError

class TransactionModelTest(TestCase):
    def setUp(self):
        self.transaction = TransactionFactory.create()

    def test_property_name(self):
        expect(self.transaction).to(have_property('pizza_id'))

    def test_property_price(self):
        expect(self.transaction).to(have_property('price'))

    def test_to_string(self):
        expect("{}".format(self.transaction)).to(equal("{}".format(self.transaction.price)))
