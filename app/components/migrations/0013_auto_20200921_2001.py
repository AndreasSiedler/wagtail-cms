# Generated by Django 3.0.10 on 2020-09-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0012_auto_20200920_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuresection',
            name='section_subheading',
            field=models.CharField(blank=True, default='What business are you?', help_text="Leave field empty to hide. <a href='/contract.pdf'>contract</a>.", max_length=100, verbose_name='Hero subtitle'),
        ),
        migrations.AlterField(
            model_name='formsection',
            name='button_action_font_weight',
            field=models.CharField(blank=True, choices=[('font-hairline', 'Hairline'), ('font-thin', 'Thin'), ('font-light', 'Light'), ('font-normal', 'Default'), ('font-hairline', 'Hailine'), ('font-medium', 'Medium'), ('font-semibold', 'Semibold'), ('font-bold', 'Bold'), ('font-extrabold', 'Extrabold'), ('font-black', 'Black')], default='font-normal', help_text='Choose font weight.', max_length=50, null=True, verbose_name='Font weight'),
        ),
        migrations.AlterField(
            model_name='formsection',
            name='section_subheading',
            field=models.CharField(blank=True, default='What business are you?', help_text="Leave field empty to hide. <a href='/contract.pdf'>contract</a>.", max_length=100, verbose_name='Hero subtitle'),
        ),
        migrations.AlterField(
            model_name='formsection',
            name='title_font_weight',
            field=models.CharField(blank=True, choices=[('font-thin', 'Thin'), ('font-light', 'Light'), ('font-normal', 'Normal'), ('font-medium', 'Medium'), ('font-bold', 'Bold')], max_length=50, null=True, verbose_name='Font Weight'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='button_action_font_weight',
            field=models.CharField(blank=True, choices=[('font-hairline', 'Hairline'), ('font-thin', 'Thin'), ('font-light', 'Light'), ('font-normal', 'Default'), ('font-hairline', 'Hailine'), ('font-medium', 'Medium'), ('font-semibold', 'Semibold'), ('font-bold', 'Bold'), ('font-extrabold', 'Extrabold'), ('font-black', 'Black')], default='font-normal', help_text='Choose font weight.', max_length=50, null=True, verbose_name='Font weight'),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='section_subheading',
            field=models.CharField(blank=True, default='What business are you?', help_text="Leave field empty to hide. <a href='/contract.pdf'>contract</a>.", max_length=100, verbose_name='Hero subtitle'),
        ),
    ]
