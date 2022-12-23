from django.db import models

class Blog(models.Model):
    blog_name = models.CharField(max_length=50)
    blog_type = models.CharField(max_length=20)
    numbers_of_comment = models.IntegerField()
    date_published = models.DateField()
    summary = models.CharField(max_length=120)


    def __str__(self):
        return self.blog_name