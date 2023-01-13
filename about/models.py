from django.db import models
from service.models import Service

class About(models.Model):
    # field = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    gender =  models.CharField(max_length=6, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    country = models.CharField(max_length= 50)
    career = models.CharField(max_length=100)
    biography = models.CharField(max_length=500)
    biography_contd = models.CharField(max_length=500)
    website = models.URLField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(null=True)
    # image = models.ImageField(blank=True)

    def __str__(self):
        fullname = self.first_name + ' ' + self.last_name
        return fullname
  
    class Meta:
        ordering = ['-id']
