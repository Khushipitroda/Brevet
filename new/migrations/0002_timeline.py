# Generated by Django 3.2.2 on 2021-06-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('tag', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]