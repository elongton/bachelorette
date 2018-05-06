from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from questions.models import Place


def reset_app(request):
    # print('hi there')
    for place in Place.objects.all():
        place.location_complete = False
        place.is_current = False
        place.save()
    #set the first location as current
    first_place = Place.objects.get(place_id=1)
    first_place.is_current = True
    first_place.save()

    return render(request, 'home.html')
