from django.apps import AppConfig

class DjangoOrganicPizzaConfig(AppConfig):
    name = 'django_organic_pizza'

    def ready(self):
        import django_organic_pizza.models
