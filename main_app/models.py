from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


    
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class UserProfile(models.Model):
    friends = models.CharField(max_length=200)

class City(models.Model):
    city = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=2500)
    date = models.DateField('date traveled')
    friends = models.ManyToManyField(UserProfile)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.city
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"city_id": self.id})
    
    class Meta:
        ordering = '-date',

class Photo(models.Model):
    url = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)