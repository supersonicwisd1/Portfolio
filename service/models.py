from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    little_detail = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.service_name

        
