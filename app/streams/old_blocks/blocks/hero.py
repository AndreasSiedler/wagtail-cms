from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from streams.blocks import default

import json

from django.forms import Media, widgets
from django.utils.functional import cached_property

from wagtail.admin.edit_handlers import RichTextFieldPanel
from wagtail.admin.rich_text.converters.contentstate import ContentstateConverter
from wagtail.admin.staticfiles import versioned_static
from wagtail.core.rich_text import features as feature_registry


class HeroDefault(blocks.StructBlock):
    layout = blocks.ChoiceBlock(
        required=True, 
        choices=[
            ('simple_centered', 'Simple centered'),
            ('image_right', 'Image on right')
        ],
        default='simple_centered',
        classname=(
            'wagtailuiplus__choice-handler'
        ))
    title = blocks.CharBlock(
        required=False, 
        help_text="Add your Title",
        classname=(
            'wagtailuiplus__show_if image_right'
        ),
    )
    title2 = blocks.CharBlock(
        required=False, 
        help_text="Add your Title",
        classname=(
            'wagtailuiplus__show_if simple_centered'
        ),
    )
    text = blocks.RichTextBlock(required=True, help_text="Add your Text")

    class Meta:
        template = "streams/hero_default_block.html"
        icon = "view"
        label = "Hero Default"
