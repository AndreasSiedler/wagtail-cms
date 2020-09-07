# Generated by Django 3.0.10 on 2020-09-07 17:47

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0024_auto_20200906_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearance',
            name='color_primary',
            field=wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose primary color.', max_length=7, null=True, verbose_name='Secondary Color'),
        ),
        migrations.AddField(
            model_name='appearance',
            name='color_secondary',
            field=wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose secondary color.', max_length=7, null=True, verbose_name='Primary Color'),
        ),
    ]