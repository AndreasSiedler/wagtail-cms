from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface

from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.blocks import StructBlock
from theme.models.buttons import ButtonAction
from .base import SectionBase


@register_snippet
class HeroSection(SectionBase, ButtonAction):

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
        on_delete=models.CASCADE,
        verbose_name='Image',
        related_name='+',
    )

    # layout tab panels
    content_tab_panels = [
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
                FieldPanel('section_heading'),
                FieldPanel('section_subheading'),
                FieldPanel('section_description'),
                FieldPanel('hero_first_button_text'),
                FieldPanel('hero_second_button_text'),
                ImageChooserPanel('hero_image'),
            ],
            heading='Content',
            classname='collapsible',
        ),
        ButtonAction.button_action_panel,
        ButtonAction.button_action_panel_advanced,
    ]

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(content_tab_panels, heading="Content"),
            ObjectList(SectionBase.advanced_tab_panels, heading="Advanced"),
        ]
    )


class HeroSectionBlock(StructBlock):

    section = SnippetChooserBlock(HeroSection)

    class Meta:
        template = 'hero_section_block.html'
        icon = 'placeholder'
        label = 'Hero Section from snippet'
