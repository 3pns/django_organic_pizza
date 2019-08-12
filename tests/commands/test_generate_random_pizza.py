from django.test import TestCase
from tests.factories import *
from expects import *
from django_organic_pizza.models import *

from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.utils.six import StringIO
import sys

class GenerateRandomPizzaCommandTest(TestCase):

    def test_call(self):
        args = []
        opts = {}
        out = StringIO()
        sys.stdout = out
        expect(out.getvalue()).to(equal(''))

    def test_unicity_collisions_on_multiple_calls(self):
        args = []
        opts = {}
        out = StringIO()
        sys.stdout = out
        call_command('generate_random_pizzas', *args, **opts, stdout=out)
        expect(out.getvalue()).to(equal(''))
        call_command('generate_random_pizzas', *args, **opts, stdout=out)
        expect(out.getvalue()).to(equal(''))
        call_command('generate_random_pizzas', *args, **opts, stdout=out)
        expect(out.getvalue()).to(equal(''))
