from django.shortcuts import *
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
