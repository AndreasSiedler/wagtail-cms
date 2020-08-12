# Generated by Django 3.0.8 on 2020-07-29 06:07

from django.db import migrations
import streams.blocks.default
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0012_auto_20200724_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('hero', wagtail.core.blocks.StreamBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('l1', 'Simple centered')])), ('title', wagtail.core.blocks.CharBlock(required=True)), ('text', streams.blocks.default.SimpleRichTextBlock())])), ('text_and_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=False)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Add your Text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Choose your Image', required=True))])), ('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional Text', required=True))])), ('full_richtext', streams.blocks.default.RichTextBlock()), ('simple_richtext', streams.blocks.default.SimpleRichTextBlock())], blank=True, null=True),
        ),
    ]