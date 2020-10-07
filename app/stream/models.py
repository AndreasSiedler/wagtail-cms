""" Stream Section """
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock


from stream.blocks import FeatureBlock
from section.sections import FormSection


class StreamPage(Page):
    """ StreamPage """
    content = StreamField(
        [
            ('feature_block', FeatureBlock()),
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
