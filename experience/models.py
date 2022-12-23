from django.db import models

class Experience(models.Model):
    work_name = models.CharField(max_length=50)
    year_started = models.CharField(max_length=4)
    year_ended_or_present = models.CharField(max_length=7)
    summary = models.CharField(max_length=350)

    def __str__(self):
        return self.work_name

    # def get_year(self):
    #     year = self.year_started[-4:]
    #     return year