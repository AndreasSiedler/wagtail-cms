from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

COLOUR_CHOICES = [
     ("red", "red-value"),
     ("blue", "blue-value")
 ]

class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(required=True,max_length=255)
    map_lat = blocks.CharBlock(required=True,max_length=255)
    map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3)
 
    class Meta:
        template = 'yourapp/blocks/google_map.html'
        icon = 'cogs'
        label = 'Google Map'

class TextAndImage(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES,default="white")
    text = blocks.CharBlock()
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-left', label='Left column content')
 
    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-right', label='Right column content')
 
    class Meta:
        template = 'yourapp/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class TitleAndText(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your Title")
    text = blocks.TextBlock(required=True, help_text="Add additional Text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"