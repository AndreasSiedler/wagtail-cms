from django.db import models
from wagtail.admin.edit_handlers import (
    MultiFieldPanel, FieldPanel, FieldRowPanel)
from section.settings import cr_settings


class SectionTitleBlock(models.Model):

    title_font_size = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['TITLE_FONT_SIZE_CHOICES'],
        verbose_name='Font Size',
        # help_text='Choose color type.',
    )
    title_font_weight = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=cr_settings['TITLE_FONT_WEIGHT_CHOICES'],
        verbose_name='Font Weight',
        # help_text='Choose color type.',
    )
    # Panels
    title_basic_panels = MultiFieldPanel(
        [
            FieldRowPanel([
                FieldPanel('title_font_size',
                           heading='Size', classname="col6"),
                FieldPanel('title_font_weight',
                           heading='Width', classname="col6"),
            ]),
        ],
        heading='Title',
    )

    class Meta:
        abstract = True
