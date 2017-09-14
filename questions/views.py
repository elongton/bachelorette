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

class ControlView(ListView):
    model = models.Place
    context_object_name = 'places'
    template_name = 'questions/control_panel.html'
    def get_context_data(self, **kwargs):
        ctx = super(ControlView, self).get_context_data(**kwargs)

        quantity_complete = models.Place.objects.filter(location_complete = True).count()
        total_quantity = models.Place.objects.count()

        try:
            currentquestion = models.Place.objects.get(is_current = True)
        except:
            currentquestion = models.Place.objects.get(place_id = total_quantity)
        currentid = currentquestion.place_id

        ctx['percentage'] = round(quantity_complete/total_quantity * 100)
        ctx['currentquestion'] = currentid
        return ctx

class PlaceDetail(DetailView):
    model = models.Place
    context_object_name = 'place'
    template_name = 'questions/placedetail.html'

    def post(self, request, *args, **kwargs):
        clue_form = ClueForm(data=request.POST)
        if clue_form.is_valid():
            answer = clue_form.cleaned_data['answer']
            place = self.get_object()
            # did someone already answer this?
            if place.location_complete == True:
                return HttpResponseRedirect(reverse("questions:control_panel"))
            else:
                answer = answer.replace(' ', '').lower()
                plankanswer = place.plank_answer.replace(' ', '').lower()

                # did they get the right answer?
                if answer == plankanswer:
                    print(answer)
                    place.location_complete = True
                    place.is_current = False
                    place.save()
                    nextplace = models.Place.objects.get(place_id = place.next_id)
                    nextplace.is_current = True
                    nextplace.save()
                    return HttpResponseRedirect(reverse("questions:success_view", kwargs={'pk':place.next_id}))
                else:
                    return HttpResponseRedirect(reverse("questions:fail_view", kwargs={'pk':place.place_id}))
                return HttpResponseRedirect(reverse("questions:control_panel"))
        else:
            return HttpResponseRedirect(reverse("questions:control_panel"))
    def get_context_data(self, **kwargs):
        ctx = super(PlaceDetail, self).get_context_data(**kwargs)
        ctx['clueform'] = ClueForm()
        return ctx



class SuccessView(TemplateView):
    template_name = 'questions/success.html'
    def get_context_data(self, **kwargs):
        ctx = super(SuccessView, self).get_context_data(**kwargs)
        ctx['nextpk'] = self.kwargs['pk']
        return ctx


class FailView(TemplateView):
    template_name = 'questions/fail.html'
    def get_context_data(self, **kwargs):
        ctx = super(FailView, self).get_context_data(**kwargs)
        ctx['samepk'] = self.kwargs['pk']
        return ctx


class ThanksView(TemplateView):
    template_name = 'questions/thanks.html'
