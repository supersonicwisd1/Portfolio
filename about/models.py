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



# class Social(models.Model):
#     phone = models.IntegerField()
#     github_web = models.URLField()
#     facebook_web = models.URLField()
#     twitter_web = models.URLField()
#     linkedin_web = models.URLField()
#     website = models.URLField()

# class Projects(models.Models):
#     project_name = models.CharField(max_length=100)
#     project_description =  models.CharField(max_length=400)

#     lang_used = models.CharField(max_length=25)
#     lang_used1 = models.CharField(max_length=25, blank=True)
#     lang_used2 = models.CharField(max_langth=25, blank=True)
#     framework = models.CharField(max_langth=25, blank=True)
#     framework1 = models.CharField(max_langth=25, blank=True)
#     framework2 = models.CharField(max_langth=25, blank=True)

#     image = models.ImageField(blank=True)