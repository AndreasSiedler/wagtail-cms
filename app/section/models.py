
import logging
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from streams.blocks import section_blocks
from wagtailmetadata.models import MetadataPageMixin

from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface

from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.blocks import StructBlock


logger = logging.getLogger(__name__)


class SectionBase(models.Model):
    title = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Title',
    )
    background_type = models.CharField(
        blank=True,
        choices=[
            ('transparent', 'Transparent'),
            ('solid', 'Solid Color'),
            ('gradient', 'Gradient Color'),
            ('image', 'Background Image'),
        ],
        max_length=100,
        help_text='Transparent background will use the background-color "page settings".',
    )
    background_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color'),
    )
    background_color_2 = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color 2'),
    )

    def __str__(self):
        if self.title:
            return self.title + " (Hero Section)"
        else:
            return super(SectionBase, self).__str__()


@register_snippet
class HeroSection(SectionBase):
    heading = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Hero title',
        default='We are heroes',
    )
    layout = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Layout',
        choices=[
            ('simple_centered', 'Simple centered'),
            ('image_right', 'Image on right')
        ],
        default='simple_centered',
    )
    subheading = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Hero subtitle',
        default='What business are you?',
        help_text="Leave field empty to hide.",
    )
    description = models.TextField(
        blank=True,
        max_length=400,
        verbose_name='Hero description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
        help_text="Leave field empty to hide.",
    )
    button_text = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Hero button text',
        default='Subscribe',
        help_text="Leave field empty to hide.",
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Image',
        related_name='+',
    )


    # layout tab panels
    content_tab_panels = [
        FieldPanel('title', heading='Title', classname='full title'),
        MultiFieldPanel(
            [
                FieldPanel('layout'),
            ],
            heading='Layout',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('subheading'),
                FieldPanel('description'),
                FieldPanel('button_text'),
                ImageChooserPanel('image'),
                # NativeColorPanel('background_color'),
            ],
            heading='Content',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [

            ],
            heading='Advanced (Coming soon)',
        )
    ]
    design_tab_panels = [
        MultiFieldPanel(
            [
                FieldPanel('background_type'),
            ],
            heading='Background type',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                NativeColorPanel('background_color'),
                NativeColorPanel('background_color_2')
            ],
            heading='Background color',
            classname='collapsible',
        )
    ]
    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(content_tab_panels, heading="Content"),
            ObjectList(design_tab_panels, heading="Design"),
        ]
    )


class HeroSectionBlock(StructBlock):

    hero_section = SnippetChooserBlock(HeroSection)

    class Meta:
        template = 'section/hero_default_block.html'
        icon = 'placeholder'
        label = 'Hero Section from snippet'


class SectionPage(MetadataPageMixin, Page):
    """ SectionPage has the normal page content and SEO panels.
    Its content additionally includes the field 'body' which can contain any number of sections via a streamfield.
    You can add stream fields other than just section blocks to the body, for example:
    ```
    from wagtail_site_sections import blocks
    body = StreamField([
        ('heading', CharBlock(required=False, label='Heading', max_length=120, help_text='', icon='arrow-right')),
        ('subheading', CharBlock(required=False, label='Subheading', max_length=120, help_text='', icon='arrow-right')),
        ('image', ImageChooserBlock(required=False, label='Image', help_text='')),
        ('quote', BlockQuoteBlock(required=False, label='Quote', help_text='')),
        ('paragraph', TextBlock(required=False, label='Paragraph', help_text='')),
    ] + blocks.section_blocks, blank=True, help_text='')
    ```
    Or you could choose only some blocks to enable for a page like so:
    ```
    body = StreamField([
        ('team_section', blocks.TeamSectionBlock()),
        ('faq_section', blocks.FaqSectionBlock()),
        ('testimonial_section', blocks.TestimonialSectionBlock()),
    ])
    ```
    body = StreamField(section_blocks + [
    ('heading', CharBlock(required=False, label='Heading', max_length=120, help_text='', icon='arrow-right')),
    ], blank=True, help_text='Add sections to the page')
    """

    body = StreamField([
        ('test', HeroSectionBlock()),
    ], blank=True, help_text='')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', heading='Page sections'),
    ]

    class Meta:
        verbose_name = 'Section Page'
        verbose_name_plural = 'Section Pages'

