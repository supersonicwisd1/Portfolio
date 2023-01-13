from django.db import models

class Education(models.Model):
    type_of_degree = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    name_of_institution = models.CharField(max_length=50)
    year_started = models.DateField()
    year_ended = models.DateField()

    def __str__(self):
        return self.type_of_degree
