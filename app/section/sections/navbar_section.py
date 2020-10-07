from django.db import models

from wagtail.admin.edit_handlers import (
    MultiFieldPanel, FieldPanel, FieldRowPanel, InlinePanel, HelpPanel)
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from section.settings import cr_settings


class NavbarSection(models.Model):
    """
    Navbar Section
    """
    navbar_layout_scheme = models.CharField(
        max_length=50,
        choices=cr_settings['NAVBAR_LAYOUT_SCHEME_CHOICES'],
        default=cr_settings['NAVBAR_LAYOUT_SCHEME_CHOICES_DEFAULT'],
        verbose_name=('Layout Scheme'),
    )
    navbar_color_scheme = models.CharField(
        max_length=50,
        choices=cr_settings['NAVBAR_COLOR_SCHEME_CHOICES'],
        default=cr_settings['NAVBAR_COLOR_SCHEME_CHOICES_DEFAULT'],
        verbose_name=('Color type'),
    )
    navbar_background_type = models.CharField(
        blank=True,
        null=True,
        choices=cr_settings['NAVBAR_BACKGROUND_TYPE_CHOICES'],
        verbose_name='Type',
        max_length=100,
    )
    navbar_background_color = ColorField(
        blank=True,
        null=True,
        verbose_name=('Color 1'),
    )
    navbar_background_color_2 = ColorField(
        blank=True,
        null=True,
        verbose_name=('Color 2'),
    )
    navbar_font_color = ColorField(
        blank=True,
        null=True,
        verbose_name=('Font color'),
    )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=('Fixed'),
    )
    navbar_transparent = models.BooleanField(
        default=False,
        verbose_name=('Transparent'),
    )
    navbar_height = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=cr_settings['NAVBAR_HEIGHT_CHOICES'],
        default=cr_settings['NAVBAR_HEIGHT_CHOICES_DEFAULT'],
        verbose_name='Height',
    )
    navbar_top_bottom_padding = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=cr_settings['NAVBAR_TOP_BOTTOM_PADDING_CHOICES'],
        default=cr_settings['NAVBAR_TOP_BOTTOM_PADDING_CHOICES_DEFAULT'],
        verbose_name='Padding',
    )
    navbar_container_width = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=cr_settings['NAVBAR_CONTAINER_WIDTH_CHOICES'],
        default=cr_settings['NAVBAR_CONTAINER_WIDTH_CHOICES_DEFAULT'],
        verbose_name='Width',
    )

    # Panels
    navbar_panels = (

        # NAVBAR
        HelpPanel(template='panels/custom_help_panel_heading.html',
                  content='Navbar'),
        MultiFieldPanel(
            (
                FieldRowPanel(
                    children=(
                        FieldPanel('navbar_transparent', classname="col6"),
                    ),
                ),
                FieldRowPanel(
                    children=(
                        FieldPanel('navbar_color_scheme', classname="col6"),
                    ),
                ),
                FieldRowPanel(children=(
                    FieldPanel('navbar_background_type', classname="col6"),
                )),
                FieldRowPanel(
                    children=(
                        NativeColorPanel('navbar_background_color',
                                         classname="col6"),
                        NativeColorPanel('navbar_background_color_2',
                                         classname="col6"),
                    ),
                ),
            ),
            heading='Design',
            classname='collapsible collapsed',
        ),
        MultiFieldPanel(
            (
                FieldRowPanel(
                    children=(
                        FieldPanel('navbar_fixed', classname="col6"),
                    ),
                ),
                FieldRowPanel(
                    children=(
                        FieldPanel('navbar_layout_scheme', classname="col6"),
                        FieldPanel('navbar_height', classname="col6"),
                        FieldPanel('navbar_container_width', classname="col6"),
                        FieldPanel('navbar_top_bottom_padding',
                                   classname="col6"),
                    ),
                ),

            ),
            heading='Layout',
            classname='collapsible collapsed',
        ),
        HelpPanel(template='panels/custom_help_panel_heading.html',
                  content=''),
    )

    class Meta:
        abstract = True
