# Generated by Django 3.0.10 on 2020-09-07 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herosection',
            name='hero_description',
        ),
        migrations.RemoveField(
            model_name='herosection',
            name='hero_heading',
        ),
        migrations.RemoveField(
            model_name='herosection',
            name='hero_layout',
        ),
        migrations.RemoveField(
            model_name='herosection',
            name='hero_subheading',
        ),
    ]