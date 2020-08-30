# Generated by Django 3.0.9 on 2020-08-26 19:32

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_socialmediasettings_header_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='header_background_color',
            field=wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose color', max_length=7, null=True),
        ),
    ]