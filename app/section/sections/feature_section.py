from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface

from wagtail.core.fields import StreamField
from . import SectionBase

from section.settings import cr_settings
from section.blocks import FeatureBlock


@register_snippet
class FeatureSection(SectionBase):
    """ Feature Section """

    feature_layout = models.CharField(
        null=True,
        max_length=50,
        choices=cr_settings['FEATURE_LAYOUT_CHOICES'],
        default=cr_settings['FEATURE_LAYOUT_CHOICES_DEFAULT'],
        verbose_name='Layout',
        # help_text='Choose font weight.',
    )
    feautre_column_count = models.CharField(
        null=True,
        max_length=50,
        choices=cr_settings['FEATURE_COLUMN_COUNT_CHOICES'],
        default=cr_settings['FEATURE_COLUMN_COUNT_CHOICES_DEFAULT'],
        verbose_name='Columns',
        # help_text='Choose font weight.',
    )
    feature_items = StreamField(
        [
            ('feature_block', FeatureBlock())
        ],
        null=True,
        verbose_name="Features",
        help_text="Please choose Features"
    )

    # layout tab panels
    # basic_tab_panels = SectionBase.section_content_panels + [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('feature_layout'),
    #             FieldPanel('feautre_column_count'),
    #         ],
    #         heading='Layout',
    #         # classname='collapsible',
    #         help_text="Please choose a feature layout!"
    #     ),
    #     MultiFieldPanel(
    #         [
    #             StreamFieldPanel('feature_items')
    #         ],
    #         heading="Features",
    #         help_text="Add feature items"
    #     )

    # ]

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(SectionBase.advanced_tab_panels, heading="Advanced"),
        ]
    )
