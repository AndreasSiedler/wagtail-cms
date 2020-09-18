# Generated by Django 3.0.10 on 2020-09-17 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('theme', '0031_auto_20200916_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appearance',
            name='feedback_form_page',
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_form_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
            ],
        ),
    ]
