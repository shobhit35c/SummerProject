# Generated by Django 4.0.6 on 2022-07-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_alter_food_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
