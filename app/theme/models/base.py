from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from theme.settings import cr_settings

from .buttons import ButtonAction


class Colors(models.Model):

    color_primary = ColorField(
        blank=True,
        null=True,
        help_text="Choose primary color.",
        verbose_name="Primary Color",
    )
    color_secondary = ColorField(
        blank=True,
        null=True,
        help_text="Choose secondary color.",
        verbose_name="Secondary Color",
    )
    
    # Panels
    color_panel = MultiFieldPanel(
        [
            NativeColorPanel('color_primary'),
            NativeColorPanel('color_secondary'),
        ],
        heading='Colors',
        classname='collapsible',
        help_text="Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    )

    class Meta:
        abstract = True


@register_setting(icon='view')
class Appearance(BaseSetting, ButtonAction, Colors):

    # Navbar settings
    navbar_layout_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES'],
        default=cr_settings['FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT'],
        verbose_name='Navbar color scheme',
        help_text='Optimizes text and other navbar elements for use with light or dark backgrounds.',
    )
    header_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=('Logo image'),
        )
    header_background_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color'),
        )
    navbar_color_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES'],
        default=cr_settings['FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT'],
        verbose_name=('Navbar color scheme'),
        help_text=('Optimizes text and other navbar elements for use with light or dark backgrounds.'),  # noqa
    )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=('Fixed navbar'),
        help_text=('Fixed navbar will remain at the top of the page when scrolling.'),
    )
    navbar_wrapper_fluid = models.BooleanField(
        default=True,
        verbose_name=('Full width navbar'),
        help_text=('The navbar will fill edge to edge.'),
    )
    navbar_content_fluid = models.BooleanField(
        default=False,
        verbose_name=('Full width navbar contents'),
        help_text=('Content within the navbar will fill edge to edge.'),
    )
    navbar_collapse_mode = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['FRONTEND_NAVBAR_COLLAPSE_MODE_CHOICES'],
        default=cr_settings['FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT'],
        verbose_name=('Collapse navbar menu'),
        help_text=('Control on what screen sizes to show and collapse the navbar menu links.'),
    )
    navbar_format = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['FRONTEND_NAVBAR_FORMAT_CHOICES'],
        default=cr_settings['FRONTEND_NAVBAR_FORMAT_DEFAULT'],
        verbose_name=('Navbar format'),
    )
    navbar_search = models.BooleanField(
        default=True,
        verbose_name=('Search box'),
        help_text=('Show search box in navbar')
    )

    # Body settings
    body_background_color_solid = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color'),
        )

    # layout tab panels
    layout_tab_panels = [
        Colors.color_panel,
        ButtonAction.button_action_panel,
        ButtonAction.button_action_panel_advanced,
        MultiFieldPanel(
            [
                FieldPanel('navbar_layout_scheme'),
                NativeColorPanel('header_background_color'),
                FieldPanel('navbar_color_scheme'),
                FieldPanel('navbar_fixed'),
                FieldPanel('navbar_wrapper_fluid'),
                FieldPanel('navbar_content_fluid'),
                FieldPanel('navbar_collapse_mode'),
                FieldPanel('navbar_format'),
                FieldPanel('navbar_search'),
            ],
            heading='Navbar',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [
                NativeColorPanel(
                    'body_background_color_solid',
                ),
            ],
            heading='Content',
            classname='collapsible collapsed',
        )
    ]
    # branding tab panels
    branding_tab_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('header_logo'),
            ],
            heading='Logo and Favicon',
            classname='collapsible',
        ),
        MultiFieldPanel(
            [

            ],
            heading='Colors',
            classname='collapsible collapsed',
        )
    ]
    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(layout_tab_panels, heading="Layout"),
            ObjectList(branding_tab_panels, heading="Branding"),
        ]
    )