from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail.core.blocks import PageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailmetadata.models import MetadataPageMixin

from components.sections import FeatureSection, HeroSection
from form.models import FormSection


class SectionPage(MetadataPageMixin, Page):
    body = StreamField(
        [
            (
                'hero_section',
                SnippetChooserBlock(
                    HeroSection,
                    icon='placeholder',
                    template='sections/hero_section.html'
                )
            ),
            (
                'feature_section',
                SnippetChooserBlock(
                    FeatureSection,
                    icon='list-ul',
                    template='sections/feature_section.html'
                )
            ),
            (
                'form_section',
                PageChooserBlock(
                    FormSection,
                    icon='list-ul',
                    template='sections/form_section.html',
                    can_choose_root=False
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
