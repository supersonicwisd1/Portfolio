# Generated by Django 3.0.1 on 2023-01-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
