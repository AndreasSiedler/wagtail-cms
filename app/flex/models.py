from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel

from streams.blocks import default, hero
from wagtailmetadata.models import MetadataPageMixin


# Create your models here.
class FlexPage(MetadataPageMixin, Page):
    intro = models.CharField(max_length=250, blank=True)
    content = StreamField(
        [
            # Custom Blocks
            ("hero", hero.HeroDefault()),
            ("text_and_image", default.TextAndImage()),
            ("title_and_text", default.TitleAndText()),
            ("full_richtext", default.RichTextBlock()),
            ("simple_richtext", default.SimpleRichTextBlock()),
        ], 
        null=True, 
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

        # ('heading', blocks.CharBlock(classname="full title")),
        # ('paragraph', blocks.RichTextBlock()),
        # ('image', ImageChooserBlock()),
        # ('row', blocks.StructBlock([
        #     ('layout', blocks.MultipleChoiceBlock(choices=[
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #         ("test", "test2"),
        #     ], widget=forms.SelectMultiple)),
        #     ('carousel', blocks.StreamBlock(
        #         [
        #             # ('columns', blocks.ListBlock([
        #             #     ('column', blocks.CharBlock()),
        #             # ])),
        #             ('image', ImageChooserBlock()),
        #             ('quotation', blocks.StructBlock([
        #                 ('text', blocks.TextBlock()),
        #                 ('author', blocks.CharBlock()),
        #             ])),
        #             ('video', EmbedBlock()),
        #         ],
        #         icon='cogs'
        #     ))
        # ], icon='user')),
