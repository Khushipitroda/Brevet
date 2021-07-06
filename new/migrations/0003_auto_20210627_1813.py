# Generated by Django 3.2.2 on 2021-06-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_timeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='pics')),
                ('type', models.CharField(choices=[('Owner', 'Owner'), ('Dealer', 'Dealer'), ('Worker', 'Worker')], default='other', max_length=50)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='role',
            field=models.CharField(choices=[('Owner', 'Owner'), ('Dealer', 'Dealer'), ('Worker', 'Worker')], default='Owner', max_length=50),
        ),
    ]
