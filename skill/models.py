from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    # skilL_grade = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    skill_grade = models.CharField(max_length=2)

    def __str__(self):
        return self.skill_name
