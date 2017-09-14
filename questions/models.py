from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Place(models.Model):
    place_id = models.PositiveIntegerField(primary_key=True)
    name_of_establishment = models.CharField(max_length=100)
    instructions = models.TextField(default='')
    plank_clue = models.TextField(default='')
    plank_answer = models.CharField(max_length=100)
    has_entered_name = models.BooleanField(default=False)
    is_current = models.BooleanField(default=False)
    location_complete = models.BooleanField(default = False)

    def __str__(self):
        return str(self.name_of_establishment)
