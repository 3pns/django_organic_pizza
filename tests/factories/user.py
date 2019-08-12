import factory
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    first_name = 'John'
    last_name = 'Doe'
    email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))

# Another, different, factory for the same object
class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'admin{0}'.format(n))
    first_name = 'Super'
    last_name = 'Doe'
    email = factory.Sequence(lambda n: 'admin{0}@example.com'.format(n))
