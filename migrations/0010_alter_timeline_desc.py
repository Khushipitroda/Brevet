# Generated by Django 3.2.2 on 2021-07-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0009_alter_home_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='desc',
            field=models.CharField(max_length=400),
        ),
    ]