from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    MultiFieldPanel, FieldPanel, StreamFieldPanel, FieldRowPanel)
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface

from wagtail.images.edit_handlers import ImageChooserPanel
from section.blocks import ButtonAction, SectionTitleBlock
from . import SectionBase
from wagtail.core.fields import StreamField
from section.blocks import ActionButton, PrimaryButton
from wagtail.core.models import Page


@register_snippet
class HeroSection(SectionBase, SectionTitleBlock, ButtonAction, Page):

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
        on_delete=models.SET_NULL,
        verbose_name='Image',
        related_name='+',
    )
    hero_buttons = StreamField(
        [
            ('action_button', ActionButton()),
            ('primary_button', PrimaryButton())
        ],
        null=True,
        verbose_name="Buttons",
        help_text="Please choose Buttons"
    )

    # basic tab panels
    basic_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('section_heading',
                               heading='Heading', classname="col6"),
                    FieldPanel('section_subheading',
                               heading='Subheading', classname="col6"),
                ]),
                FieldRowPanel([
                    FieldPanel('section_description',
                               heading='Description', classname="col6"),
                ]),
                FieldPanel('hero_first_button_text'),
                FieldPanel('hero_second_button_text'),
                ImageChooserPanel('hero_image'),

            ],
            heading='Content',
        ),


        SectionBase.section_layout_panels,
        SectionBase.section_design_panels,

    ]

    # advanced tab panels
    advanced_panels = (
        SectionTitleBlock.title_basic_panels,
    ) + ButtonAction.button_action_panels

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(basic_panels, heading="Basic"),
            ObjectList(advanced_panels, heading="Plus+"),

        ]
    )

    # Page settings
    template = 'sections/hero_section_preview.html'
    parent_page_types = ['home.HomePage']
    subpage_types = []

    # Overring methods
    def set_url_path(self, parent):
        """
        Populate the url_path field based on this page's slug and the specified parent page.
        (We pass a parent in here, rather than retrieving it via get_parent, so that we can give
        new unsaved pages a meaningful URL when previewing them; at that point the page has not
        been assigned a position in the tree, as far as treebeard is concerned.
        """
        if parent:
            self.url_path = ''
        else:
            # a page without a parent is the tree root, which always has a url_path of '/'
            self.url_path = '/'

        return self.url_path
