from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .models import AboutMeModel

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'strGiorgio'
        context['AboutMeModel'] = AboutMeModel.objects.all()
        return context