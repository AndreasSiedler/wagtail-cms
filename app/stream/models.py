""" Stream Section """
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import StructBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from stream.section_blocks import (HeroBaseBlock, SectionHeadingBlock, SectionSubheadingBlock,
                                   SectionDescriptionBlock, HeroImageBlock, FeatureBaseBlock, FeatureItemsBlock)
from section.sections import FormSection


class FeatureSectionBlock(StructBlock):
    """ Feature Block """
    base = FeatureBaseBlock()
    heading = SectionHeadingBlock()
    subheading = SectionSubheadingBlock()
    description = SectionDescriptionBlock()
    items = FeatureItemsBlock()

    class Meta:
        """ Meta data """
        form_template = 'block_forms/multi_field.html'
        template = 'block_sections/feature_section.html'
        icon = 'tick'
        label = 'Feature Section'


class HeroSectionBlock(StructBlock):
    """ Hero Block """
    base = HeroBaseBlock()
    heading = SectionHeadingBlock()
    subheading = SectionSubheadingBlock()
    description = SectionDescriptionBlock()
    image = HeroImageBlock()

    class Meta:
        """ Meta data """
        form_template = 'block_forms/multi_field.html'
        template = 'block_sections/hero_section.html'
        icon = 'placeholder'
        label = 'Hero Section'


class StreamPage(Page):
    """ StreamPage """
    content = StreamField(
        [
            ('hero_section_block', HeroSectionBlock()),
            ('feature_section_block', FeatureSectionBlock()),
            ('form_section', SnippetChooserBlock(
                FormSection,
                icon='doc-empty-inverse',
                template='sections/form_section.html',
                can_choose_root=False)),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]
