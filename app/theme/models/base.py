from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from components.models import ButtonAction
from .navbar import Navbar
from .footer import Footer


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
class Appearance(BaseSetting, Navbar, Footer, ButtonAction, Colors):

    # Navbar settings
    header_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=('Logo image'),
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
        # PageChooserPanel('feedback_form_page', ['form.FormSection']),
        Colors.color_panel,
        ButtonAction.button_action_panel,
        ButtonAction.button_action_panel_advanced,
        Navbar.navbar_panel,
        Footer.footer_panel,
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
