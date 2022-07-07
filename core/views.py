from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .models import AboutMeModel, IdiomsModel, KnowledgesModel, SkillsModel
from .forms import UsersMessagesForm

# Create your views here.
class IndexView(FormView):
    template_name = 'index.html'
    form_class = UsersMessagesForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['title'] = 'strGiorgio'
        
        context['AboutMeModel'] = AboutMeModel.objects.all()

        context['IdiomsModel'] = IdiomsModel.objects.order_by('?').all()

        context['SkillsModel'] = SkillsModel.objects.order_by('?').all()
        context['SkillsModelCount'] = SkillsModel.objects.count()

        context['KnowledgesModel'] = KnowledgesModel.objects.order_by('?').all()
        context['KnowledgesModelCount'] = KnowledgesModel.objects.count()

        context['form'] = UsersMessagesForm
        return context
    

    def form_valid(self, form, *args, **kwargs):
        form.save()
        print('Message sended!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        print('Message not sended!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)