
import logging
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

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
from theme.models.buttons import ButtonAction


logger = logging.getLogger(__name__)


class MyMixin(object):

    def __init__(self, new_arg=None, *args, **kwargs):
        self.new_arg = new_arg
        super(MyMixin, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(MyMixin, self).deconstruct()
        if self.new_arg is not None:
            kwargs['new_arg'] = self.new_arg
        return name, path, args, kwargs


class MyMixinCharField(MyMixin, models.CharField):
    pass


class MyMixinAbsctractModelTest(models.Model):
    myfield = MyMixinCharField(
        max_length=512,
        new_arg="myarg",
        db_column='new_myfield'
    )


class WrapperBase(models.Model):
    padding_top = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        # db_column='new_padding_top'
    )

    # Define abstract to dont create own database table for this model - fields are created in the child class
    class Meta:
        abstract = True


class SectionBase(models.Model):
    section_name = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Title',
    )
    section_background_type = models.CharField(
        blank=True,
        null=True,
        choices=[
            ('transparent', 'Transparent'),
            ('solid', 'Solid Color'),
            ('gradient', 'Gradient Color'),
            ('image', 'Background Image'),
        ],
        default='trasparent',
        max_length=100,
        help_text='Transparent background will use the background-color "page settings".',
    )
    section_background_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color'),
    )
    section_background_color_2 = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color 2'),
    )
    design_tab_panels = [
        MultiFieldPanel(
            [
                FieldPanel('section_background_type'),
            ],
            heading='Background type',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                NativeColorPanel('section_background_color'),
                NativeColorPanel('section_background_color_2')
            ],
            heading='Background color',
            classname='collapsible',
        )
    ]

    # Define abstract to dont create own database table for this model - fields are created in the child class
    class Meta:
        abstract = True

    def __str__(self):
        if self.section_name:
            return self.section_name + " (Hero Section)"
        else:
            return super(SectionBase, self).__str__()


@register_snippet
class HeroSection(SectionBase, ButtonAction):
    hero_subheading = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Hero subtitle',
        default='What business are you?',
        help_text="Leave field empty to hide.",
    )
    hero_heading = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Hero title',
        default='We are heroes',
    )
    hero_layout = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Layout',
        choices=[
            ('simple_centered', 'Simple centered'),
            ('image_right', 'Image on right')
        ],
        default='simple_centered',
    )
    hero_description = models.TextField(
        blank=True,
        max_length=400,
        verbose_name='Hero description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
        help_text="Leave field empty to hide.",
    )
    hero_first_button_text = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Hero button text',
        default='Subscribe',
        help_text="Leave field empty to hide.",
    )
    hero_second_button_text = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Hero button text',
        default='Subscribe',
        help_text="Leave field empty to hide.",
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Image',
        related_name='+',
    )

    # layout tab panels
    content_tab_panels = [
        ButtonAction.button_action_panel,
        FieldPanel('section_name', heading='Name', classname='full title'),
        MultiFieldPanel(
            [
                FieldPanel('hero_layout'),
            ],
            heading='Layout',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_subheading'),
                FieldPanel('hero_description'),
                FieldPanel('hero_first_button_text'),
                FieldPanel('hero_second_button_text'),
                ImageChooserPanel('hero_image'),
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

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(content_tab_panels, heading="Content"),
            ObjectList(SectionBase.design_tab_panels, heading="Design"),
        ]
    )


class HeroSectionBlock(StructBlock):

    section = SnippetChooserBlock(HeroSection)

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
