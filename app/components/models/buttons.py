from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from components.settings import cr_settings


class ButtonAction(models.Model):

    button_action_bg_color_type = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_COLOR_TYPE_CHOICES'],
        default=cr_settings['BUTTON_COLOR_TYPE_CHOICES_DEFAULT'],
        verbose_name='Color Type',
        help_text='Choose color type.',
    )
    button_action_bg_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose background color.",
        verbose_name=('Color'),
    )
    button_action_bg_color_hover = ColorField(
        blank=True,
        null=True,
        help_text="Choose hover background color",
        verbose_name=('Color (hover)'),
    )
    button_action_text_color = ColorField(
        blank=True,
        null=True,
        help_text="Choose text color.",
        verbose_name="Text color"
    )
    button_action_text_color_hover = ColorField(
        blank=True,
        null=True,
        help_text="Choose text hover color.",
        verbose_name="Text color (hover)"
    )
    button_action_font_weight = models.CharField(
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_FONT_WEIGHT_CHOICES'],
        default=cr_settings['BUTTON_FONT_WEIGHT_CHOICES_DEFAULT'],
        verbose_name='Font weight',
        help_text='Choose font weight.',
    )
    button_action_padding = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_PADDING_COICES'],
        # default=cr_settings['BUTTON_PADDING_COICES_DEFAULT'],
        verbose_name='Size',
        help_text='Choose button size.',
    )
    button_action_border_radius = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_BORDER_RADIUS_COICES'],
        # default=cr_settings['BUTTON_BORDER_RADIUS_COICES_DEFAULT'],
        verbose_name='Edges',
        help_text='Choose button edges.',
    )
    
    # Panels
    button_action_panel = MultiFieldPanel(
        [
            FieldPanel('button_action_padding'),
            FieldPanel('button_action_border_radius'),
            FieldPanel('button_action_font_weight'),
        ],
        heading='Action Button (CTA)',
        classname='collapsible',
        help_text="A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do."
    )
    button_action_panel_advanced = MultiFieldPanel(
        [
            FieldPanel('button_action_bg_color_type'),
            NativeColorPanel('button_action_bg_color'),
            NativeColorPanel('button_action_bg_color_hover'),
            NativeColorPanel('button_action_text_color'),
            NativeColorPanel('button_action_text_color_hover'),
        ],
        heading='Action Button (Advanced)',
        classname='collapsible collapsed'
    )

    class Meta:
        abstract = True
