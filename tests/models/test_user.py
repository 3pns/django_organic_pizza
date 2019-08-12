from django.test import TestCase
from tests.factories import *
from expects import *

class UserModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create()

    def test_property_username(self):
        expect(self.user).to(have_property('username'))

    def test_property_first_name(self):
        expect(self.user).to(have_property('first_name'))
    
    def test_property_last_name(self):
        expect(self.user).to(have_property('last_name'))
