# Generated by Django 5.0 on 2023-12-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, max_length=120),
        ),
    ]
