from django.db import models

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, FieldRowPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from section.settings import cr_settings


class Navbar(models.Model):
    navbar_color_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['NAVBAR_COLOR_SCHEME_CHOICES'],
        default=cr_settings['NAVBAR_COLOR_SCHEME_CHOICES_DEFAULT'],
        verbose_name=('Color type'),
        # help_text=('A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do.'),  # noqa
    ),
    navbar_layout_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=cr_settings['NAVBAR_LAYOUT_SCHEME_CHOICES'],
        default=cr_settings['NAVBAR_LAYOUT_SCHEME_CHOICES_DEFAULT'],
        verbose_name=('Color type'),
        # help_text=('A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do.'),  # noqa
    )
    navbar_background_color = ColorField(
        blank=True,
        null=True,
        # help_text="Choose background color",
        verbose_name=('Background color'),
    )
    navbar_font_color = ColorField(
        blank=True,
        null=True,
        # help_text="Choose font color",
        verbose_name=('Font color'),
    )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=('Fixed'),
        # help_text=(
        #     'Fixed navbar will remain at the top of the page when scrolling.'),
    )
    navbar_transparent = models.BooleanField(
        default=False,
        verbose_name=('Transparent'),
        # help_text=(
        #     'Transparent background on top.'),
    )
    navbar_panel = MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('navbar_color_scheme', classname="col6"),
            ]),
            FieldRowPanel([
                FieldPanel('navbar_fixed', classname="col6"),
                FieldPanel('navbar_transparent', classname="col6"),
                NativeColorPanel('navbar_background_color', classname="col6"),
                NativeColorPanel('navbar_font_color', classname="col6"),
            ]),
        ],
        heading='Navbar',
        help_text="A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do."
    )

    class Meta:
        abstract = True
