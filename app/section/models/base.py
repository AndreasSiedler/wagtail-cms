from django.db import models

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class SectionBase(models.Model):
    section_name = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Title',
    )
    section_heading = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Hero title',
        default='We are heroes',
    )
    section_subheading = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Hero subtitle',
        default='What business are you?',
        help_text="Leave field empty to hide.",
    )
    section_description = models.TextField(
        blank=True,
        max_length=400,
        verbose_name='Hero description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
        help_text="Leave field empty to hide.",
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
        verbose_name=('Color 1'),
    )
    section_background_color_2 = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Color 2'),
    )
    section_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Background image',
        related_name='+',
    )

    # Panels
    design_tab_panels = [
        MultiFieldPanel(
            [
                FieldPanel('section_background_type'),
            ],
            heading='Background > Type',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                NativeColorPanel('section_background_color'),
                NativeColorPanel('section_background_color_2'),
            ],
            heading='Background > Color',
            classname='collapsible',
            help_text="Please select Background Type first."
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel('section_background_image'),
            ],
            heading='Background > Image',
            classname='collapsible',
        ),
    ]

    # Define abstract to dont create own database table for this model - fields are created in the child class
    class Meta:
        abstract = True

    def __str__(self):
        if self.section_name:
            return self.section_name + " (Hero Section)"
        else:
            return super(SectionBase, self).__str__()

