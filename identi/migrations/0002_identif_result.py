# Generated by Django 5.0.6 on 2024-05-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identif',
            name='result',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
