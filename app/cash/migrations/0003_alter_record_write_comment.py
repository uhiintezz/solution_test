# Generated by Django 5.1.6 on 2025-02-07 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='write_comment',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
