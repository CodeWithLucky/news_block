# Generated by Django 5.0.2 on 2024-02-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmod',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
