from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Fish(models.Model):
    species = models.CharField(max_length=20)
    angler = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default= 0)
    description = models.TextField(default='')

    def __str__(self):
        return_string = f'{self.species}'
        # return self.species
        return return_string
    
    def get_absolute_url(self):
        return reverse('fish_detail', args=[str(self.id)])
