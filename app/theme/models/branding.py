from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel


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
