# Generated by Django 3.0.1 on 2022-12-10 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_of_work', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Work')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('views', models.PositiveIntegerField()),
                ('likes', models.PositiveIntegerField()),
                ('project_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Tags')),
            ],
        ),
    ]
