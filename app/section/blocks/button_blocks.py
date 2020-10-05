from django.db import models
from django.utils.safestring import mark_safe

from wagtail.admin.edit_handlers import (
    MultiFieldPanel, FieldPanel, FieldRowPanel, HelpPanel)
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from section.settings import cr_settings


class ButtonAction(models.Model):

    button_action_bg_color_type = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_COLOR_TYPE_CHOICES'],
        default=cr_settings['BUTTON_COLOR_TYPE_CHOICES_DEFAULT'],
        verbose_name='Type',
        help_text=mark_safe(
            'Define primary and secondarz color in tab <a href="./#tab-branding">here</a>.'),
    )
    button_action_bg_color = ColorField(
        blank=True,
        null=True,
        help_text="Disable 'Color Type' to activate this field.",
        verbose_name='Color',
    )
    button_action_bg_color_hover = ColorField(
        blank=True,
        null=True,
        # help_text="Choose hover background color",
        verbose_name='On hover',
    )
    button_action_text_color = ColorField(
        blank=True,
        null=True,
        # help_text="Choose text color.",
        verbose_name="Color"
    )
    button_action_text_color_hover = ColorField(
        blank=True,
        null=True,
        # help_text="Choose text hover color.",
        verbose_name="On hover"
    )
    button_action_font_weight = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_FONT_WEIGHT_CHOICES'],
        default=cr_settings['BUTTON_FONT_WEIGHT_CHOICES_DEFAULT'],
        verbose_name='Weight',
        # help_text='Choose font weight.',
    )
    button_action_padding = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_PADDING_COICES'],
        # default=cr_settings['BUTTON_PADDING_COICES_DEFAULT'],
        verbose_name='Size',
        # help_text='Choose button size.',
    )
    button_action_border_radius = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['BUTTON_BORDER_RADIUS_COICES'],
        # default=cr_settings['BUTTON_BORDER_RADIUS_COICES_DEFAULT'],
        verbose_name='Edges',
        # help_text='Choose button edges.',
    )

    # Panels
    # button_action_panel = MultiFieldPanel(
    #     [
    #         FieldRowPanel([
    #             FieldPanel('button_action_bg_color_type', classname="col6"),
    #             NativeColorPanel('button_action_bg_color', classname="col6"),
    #         ]),
    #         FieldRowPanel([
    #             FieldPanel('button_action_padding', classname="col6"),
    #             FieldPanel('button_action_border_radius', classname="col6"),
    #             FieldPanel('button_action_font_weight', classname="col6"),
    #             NativeColorPanel(
    #                 'button_action_bg_color_hover', classname="col6"),
    #             NativeColorPanel('button_action_text_color', classname="col6"),
    #             NativeColorPanel(
    #                 'button_action_text_color_hover', classname="col6"),
    #         ]),

    #     ],
    #     heading='Action Button',
    #     help_text="A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do."
    # )

    button_action_panels = (
        HelpPanel(template='panels/custom_help_panel_template.html',
                  content='Action Button', ),
        # Color
        MultiFieldPanel(
            (
                FieldRowPanel(
                    children=(
                        FieldPanel('button_action_bg_color_type',
                                   classname="col6"),
                        NativeColorPanel(
                            'button_action_bg_color', classname="col6"),
                        NativeColorPanel(
                            'button_action_bg_color_hover', classname="col6"),
                    ),
                ),
            ),
            heading='Color',
            classname='collapsible',
        ),
        # Layout
        MultiFieldPanel(
            (
                FieldRowPanel(
                    children=(
                        FieldPanel('button_action_padding', classname="col6"),
                        FieldPanel('button_action_border_radius',
                                   classname="col6"),
                    )
                ),
            ),
            heading='Layout',
            classname='collapsible',
        ),
        # Text
        MultiFieldPanel(
            (
                FieldRowPanel(
                    children=(
                        FieldPanel('button_action_font_weight',
                                   classname="col6"),
                        NativeColorPanel(
                            'button_action_text_color', classname="col6"),
                        NativeColorPanel(
                            'button_action_text_color_hover', classname="col6"),
                    )
                ),
            ),
            heading='Text',
            classname='collapsible',
        ),
    )

    class Meta:
        abstract = True
