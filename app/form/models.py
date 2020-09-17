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


class FormField(AbstractFormField):
    page = ParentalKey('FormSection', on_delete=models.CASCADE, related_name='form_fields')


class FormIndexPage(Page):
    parent_page_types = []


class FormSection(MetadataPageMixin, AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    parent_page_types = ['form.FormIndexPage']

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

    template = 'form/form_section_preview.html'

    def __str__(self):
        if self.title:
            return self.title + " (Form Section)"
        else:
            return super(AbstractEmailForm, self).__str__()
