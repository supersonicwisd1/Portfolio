from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=25, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.tag

class Category(models.Model):
    category = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.category

class Work(models.Model):
    project_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name='tags')
    section = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="categories")
    project_name = models.CharField(max_length=20, blank=True)
    views = models.PositiveIntegerField(null=True)
    likes = models.PositiveIntegerField(null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.project_name
