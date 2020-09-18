from django.db import models

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from theme.settings import cr_settings


class Navbar(models.Model):
    navbar_color_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES'],
        default=cr_settings['FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT'],
        verbose_name=('Color scheme'),
        help_text=('A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do.'),  # noqa
    )
    navbar_background_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color",
        verbose_name=('Background color'),
        )
    navbar_font_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose font color",
        verbose_name=('Font color'),
        )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=('Fixed'),
        help_text=('Fixed navbar will remain at the top of the page when scrolling.'),
    )
    navbar_transparent = models.BooleanField(
        default=False,
        verbose_name=('Transparent'),
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
    # Panels
    navbar_panel = MultiFieldPanel(
        [
            FieldPanel('navbar_color_scheme'),
            FieldPanel('navbar_fixed'),
            FieldPanel('navbar_transparent'),
        ],
        heading='Navbar',
        classname='collapsible',
        help_text="A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do."
    )
    navbar_panel_advanced = MultiFieldPanel(
        [
            NativeColorPanel('navbar_background_color'),
            NativeColorPanel('navbar_font_color'),
            FieldPanel('navbar_wrapper_fluid'),
            FieldPanel('navbar_content_fluid'),
            FieldPanel('navbar_collapse_mode'),
            FieldPanel('navbar_format'),
            FieldPanel('navbar_search'),
        ],
        heading='Navbar Advanced',
        classname='collapsible',
        help_text="A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do."
    )

    class Meta:
        abstract = True
