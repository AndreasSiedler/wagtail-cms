# Generated by Django 3.0.10 on 2020-09-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20200905_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='herosection',
            name='padding_top',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
    ]