from django import forms
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  CreateView, DetailView,
                                  ListView)
from . import models
from .forms import ClueForm
# Create your views here.

class ControlView(TemplateView):
    template_name = 'questions/control_panel.html'



class PlaceDetail(DetailView):
    model = models.Place
    context_object_name = 'place'
    template_name = 'questions/placedetail.html'

    def post(self, request, *args, **kwargs):
        clue_form = ClueForm(data=request.POST)
        if clue_form.is_valid():
            answer = clue_form.cleaned_data['answer']
            place = self.get_object()
            if answer == place.name_of_establishment:
                print('YAY!')
            else:
                print('nope')
            # print(answer)
            return HttpResponseRedirect(reverse("questions:control_panel"))
        else:
            return HttpResponseRedirect(reverse("questions:control_panel"))
    def get_context_data(self, **kwargs):
        ctx = super(PlaceDetail, self).get_context_data(**kwargs)
        ctx['clueform'] = ClueForm()
        return ctx
