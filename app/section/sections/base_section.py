from django.db import models
from django.utils.safestring import mark_safe

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel, FieldPanel, FieldRowPanel)
from wagtail.images.edit_handlers import ImageChooserPanel

from section.settings import cr_settings


class SectionBase(models.Model):
    # Content
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
        null=True,
        max_length=100,
        verbose_name='Hero subtitle',
        default='What business are you?',
        help_text=mark_safe(
            "Leave field empty to hide. <a href='/contract.pdf'>contract</a>.")
    )
    section_description = models.TextField(
        blank=True,
        null=True,
        max_length=400,
        verbose_name='Hero description',
        default=('The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.'),
        help_text="Leave field empty to hide.",
    )
    # Background
    section_background_type = models.CharField(
        blank=True,
        null=True,
        choices=[
            ('transparent', 'Transparent'),
            ('solid', 'Solid Color'),
            ('gradient', 'Gradient Color'),
            ('image', 'Background Image'),
        ],
        verbose_name='Type',
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
        on_delete=models.SET_NULL,
        verbose_name='Image',
        related_name='+',
    )
    # Layout
    section_color_theme = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=cr_settings['SECTION_COLOR_THEME_CHOICES'],
        verbose_name='Theme',
        # help_text='Choose font weight.',
    )
    section_top_bottom_padding = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=cr_settings['SECTION_TOP_BOTTOM_PADDING_CHOICES'],
        default=cr_settings['SECTION_TOP_BOTTOM_PADDING_CHOICES_DEFAULT'],
        verbose_name='Height',
        # help_text='Choose font weight.',
    )
    section_container_width = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=cr_settings['SECTION_CONTAINER_WIDTH_CHOICES'],
        default=cr_settings['SECTION_CONTAINER_WIDTH_CHOICES_DEFAULT'],
        verbose_name='Width',
        # help_text='Choose font weight.',
    )

    # Basic Panels
    section_content_panels = MultiFieldPanel(
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

        ],
        heading='Content',
    )

    section_layout_panels = MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('section_top_bottom_padding',
                           heading='Size', classname="col6"),
                FieldPanel('section_container_width',
                           heading='Width', classname="col6"),
            ]),
            FieldRowPanel([
                FieldPanel('section_color_theme',
                           heading='Theme', classname="col6"),
            ]),
        ],
        heading='Layout',
    )

    section_design_panels = MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('section_background_type',
                           heading='Type', classname="col6"),
            ]),
            FieldRowPanel([
                NativeColorPanel('section_background_color',
                                 heading='Color 1', classname="col6"),
                NativeColorPanel('section_background_color_2',
                                 heading='Color 2', classname="col6"),
            ]),
            FieldRowPanel([
                ImageChooserPanel('section_background_image',
                                  heading='Image'),
            ]),
        ],
        heading='Design',
    )

    # Legacy
    advanced_tab_panels = [
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
