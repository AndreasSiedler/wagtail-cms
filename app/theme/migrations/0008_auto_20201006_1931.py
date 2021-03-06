# Generated by Django 3.1.2 on 2020-10-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0007_remove_appearance_navbar_background_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearance',
            name='navbar_container_width',
            field=models.CharField(blank=True, choices=[('container max-w-2xl', 'Small'), ('container max-w-4xl', 'Medium'), ('container', 'Large'), ('container max-w-full', 'Full')], default='container', max_length=50, null=True, verbose_name='Width'),
        ),
        migrations.AddField(
            model_name='appearance',
            name='navbar_top_bottom_padding',
            field=models.CharField(blank=True, choices=[('py-0', 'None'), ('py-24', 'Small'), ('py-40', 'Medium'), ('py-56', 'Large'), ('py-64', 'X-Large')], default='py-40', max_length=50, null=True, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='appearance',
            name='navbar_background_type',
            field=models.CharField(blank=True, choices=[('solid', 'Solid Color'), ('gradient', 'Gradient Color')], max_length=100, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='appearance',
            name='navbar_color_scheme',
            field=models.CharField(choices=[('light_basic', 'Light'), ('dark_basic', 'Dark')], default='light', max_length=50, verbose_name='Color type'),
        ),
        migrations.AlterField(
            model_name='appearance',
            name='navbar_layout_scheme',
            field=models.CharField(choices=[('logo_left_nav_right', 'Simple right'), ('logo_left_nav_right', 'Simple left')], default='light', max_length=50, verbose_name='Layout Scheme'),
        ),
    ]
