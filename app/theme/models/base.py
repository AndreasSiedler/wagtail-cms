from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, FieldRowPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from components.blocks import ButtonAction
from components.sections import Navbar
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
        verbose_name=('Logo Image'),
    )

    favicon_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=('Favicon'),
    )

    # Body settings
    body_background_color_solid = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color'),
    )

    # components tab panels
    components_panels = [
        # PageChooserPanel('feedback_form_page', ['form.FormSection']),
        ButtonAction.button_action_panel,
        Navbar.navbar_panel,
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
    branding_panels = [
        MultiFieldPanel(
            [
                FieldRowPanel([
                    NativeColorPanel('color_primary',
                                     heading='Color 1', classname="col6"),
                    NativeColorPanel('color_secondary',
                                     heading='Color 2', classname="col6"),
                ]),
            ],
            heading='Colors',
        ),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    ImageChooserPanel(
                        'header_logo', heading='Logo', classname="col12"),
                    ImageChooserPanel(
                        'favicon_image', heading='Favicon', classname="col12"),
                ]),
            ],
            heading='Logo and Favicon',
        ),
    ]
    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(branding_panels, heading="Branding"),
            ObjectList(components_panels, heading="Components"),
        ]
    )
