from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtailmetadata.models import MetadataPageMixin
from streams.blocks import HeroSectionChooserBlock


class SectionPage(MetadataPageMixin, Page):
    body = StreamField(
        [
            ('test', HeroSectionChooserBlock()),
        ],
        blank=True,
        help_text=''
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('body', heading='Page sections'),
    ]

    class Meta:
        verbose_name = 'Section Page'
        verbose_name_plural = 'Section Pages'
