# Generated by Django 3.2.2 on 2021-07-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0012_alter_product_pdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='potype',
            field=models.CharField(choices=[('Special_Ink', 'Special_Ink'), ('Screen_Chemicals', 'Screen_Chemicals'), ('other', 'other')], default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ptype',
            field=models.CharField(choices=[('Special_Ink', 'Special_Ink'), ('Screen_Chemicals', 'Screen_Chemicals'), ('other', 'other')], default='other', max_length=50),
        ),
    ]
