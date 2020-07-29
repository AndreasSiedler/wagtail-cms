from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TextAndImage(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text="Add your Title")
    text = blocks.RichTextBlock(required=True, help_text="Add your Text")
    image = ImageChooserBlock(required=True, help_text="Choose your Image")

    class Meta:
        template = "streams/text_image_block.html"
        icon = "view"
        label = "Text and Image"

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