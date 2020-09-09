from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailmetadata.models import MetadataPageMixin

from snippets.sections import FeatureSection, HeroSection


class SectionPage(MetadataPageMixin, Page):
    body = StreamField(
        [
            (
                'hero_section',
                SnippetChooserBlock(
                    HeroSection,
                    icon='placeholder',
                    template='hero_section.html'
                )
            ),
            (
                'feature_section',
                SnippetChooserBlock(
                    FeatureSection,
                    icon='list-ul',
                    template='feature_section.html'
                )
            ),
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
