# Generated by Django 5.0.6 on 2024-06-02 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identi', '0003_alter_identif_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identif',
            old_name='data',
            new_name='file',
        ),
    ]
