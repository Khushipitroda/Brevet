# Generated by Django 3.2.2 on 2021-07-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0010_alter_timeline_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ptype',
            field=models.CharField(choices=[('Special_Ink', 'Special_Ink'), ('Screen_Chemicals', 'Screen_Chemicals'), ('Textile_Emulsions', 'Textile_Emulsions'), ('Graphics_Emulsions', 'Graphics_Emulsions'), ('other', 'other')], default='other', max_length=50),
        ),
    ]
