from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtailmetadata.models import MetadataPageMixin
from .base import SectionBase

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import ObjectList, TabbedInterface


class FormField(AbstractFormField):
    page = ParentalKey('FormSection', on_delete=models.CASCADE, related_name='form_fields')


class FormIndexPage(Page):
    # parent_page_types = []
    parent_page_types = ['home.HomePage']
    max_count = 1


class FormSection(SectionBase, MetadataPageMixin, AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    parent_page_types = ['components.FormIndexPage']

    # layout tab panels
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    basic_tab_panels = SectionBase.basic_tab_panels

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(basic_tab_panels, heading="Design"),
            ObjectList(SectionBase.advanced_tab_panels, heading="Advanced"),
        ]
    )

    # Preview Template
    template = 'sections/form_section_preview.html'

    # Overriding Methods
    def serve(self, request):
        if request.is_ajax():
            print('IS AXJAX')
        return super(FormSection, self).serve(request)

    def __str__(self):
        if self.title:
            return self.title + " (Form Section)"
        else:
            return super(AbstractEmailForm, self).__str__()
