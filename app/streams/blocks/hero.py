from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from streams.blocks import default

class HeroDefault(blocks.StructBlock):
    layout = blocks.ChoiceBlock(required=True, choices=[
        ('simple_centered', 'Simple centered'),
        ('image_right', 'Image on right')
    ], default='simple_centered')
    title = blocks.CharBlock(required=False, help_text="Add your Title")
    text = blocks.RichTextBlock(required=True, help_text="Add your Text")

    class Meta:
        template = "streams/hero_default_block.html"
        icon = "view"
        label = "Hero Default"


