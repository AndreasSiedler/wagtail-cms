from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    MultiFieldPanel, FieldPanel, StreamFieldPanel, FieldRowPanel)
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface

from wagtail.images.edit_handlers import ImageChooserPanel
from section.blocks import ButtonAction, SectionTitleBlock
from . import SectionBase
from wagtail.core.fields import StreamField
from section.blocks import ActionButton, PrimaryButton
from wagtail.core.models import Page


@register_snippet
class HTMLSection(Page):

    html_content = models.TextField(
        blank=True,
        null=True,
        max_length=400,
        verbose_name='Hero description',
        default=('The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.'),
        help_text="Leave field empty to hide.",
    )
   