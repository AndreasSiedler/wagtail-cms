from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel


# Create your models here.
@register_setting
class SocialMediaSettings(BaseSetting):
    """" Social media settings for our custom webite """

    facebook = models.URLField(blank=True, null=True, help_text="Facebook Url")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter Url")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube Url")

    header_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    header_background_color = ColorField(blank=True, null=True, help_text="Choose background color")

    header_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('header_logo'),
                NativeColorPanel('header_background_color'),
            ]
        )
    ]

    socia_media_panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ])
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(socia_media_panels, heading="Social"),
            ObjectList(header_panels, heading="Header"),
        ]
    )


# register_setting(SocialMediaSettings)
