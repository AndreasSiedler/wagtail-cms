# Generated by Django 3.0.10 on 2020-09-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20200920_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsection',
            name='form_submit_button_text',
            field=models.CharField(blank=True, default='Submit', max_length=100, verbose_name='Submit button text'),
        ),
    ]
