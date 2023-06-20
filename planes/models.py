from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Plane(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=False, blank=True, default='')
    Cost = models.CharField(max_length=255, null=False, blank=True, default='')
    Speed = models.CharField(max_length=255, null=False, blank=True, default='')
    Year_Published = models.CharField(max_length=255, null=False, blank=True, default='')
    Reviewer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
            return self.name
    
    def get_absolute_url(self):
        return reverse('plane_list')