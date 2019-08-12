from django.shortcuts import *
from django.views.generic import TemplateView
from django_organic_pizza.models import Pizza
from django.db import connection
from django.db.models import Count, Sum
from django.conf import settings

class Index(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        pizzas = Pizza.objects.prefetch_related("transactions", "pizza_type") \
                              .annotate(total_sold=Count('transactions')) \
                              .annotate(total_amount=Sum('transactions__price')) \
                              .order_by('-total_sold')
        return render(request, self.template_name, {'pizzas': pizzas, 'timezone': settings.TIME_ZONE})
