# Generated by Django 4.0.3 on 2022-04-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city_birth',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_creator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_visitor',
            field=models.BooleanField(default=False),
        ),
    ]