from django.db import models
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from components.sections import SectionBase
from components.blocks import SectionTitleBlock, ButtonAction

from wagtail.admin.edit_handlers import ObjectList, TabbedInterface
from components.settings import cr_settings


class FormField(AbstractFormField):
    page = ParentalKey('FormSection', on_delete=models.CASCADE,
                       related_name='form_fields')
    field_layout = models.CharField(
        null=True,
        max_length=50,
        choices=cr_settings['FORM_FIELD_WIDTH_CHOICES'],
        default=cr_settings['FORM_FIELD_WIDTH_CHOICES_DEFAULT'],
        verbose_name='Field width',
        # help_text='Choose font weight.',
    )

    # Add additional field panels
    panels = AbstractFormField.panels + [
        FieldPanel('field_layout'),
    ]


class FormIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['components.FormSection']
    max_count = 1


@register_snippet
class FormSection(SectionBase, SectionTitleBlock, ButtonAction, AbstractEmailForm):

    form_submit_button_text = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Submit button text',
        default='Submit',
        # help_text="Leave field empty to hide.",
    )
    # intro = RichkTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    # basic tab panels
    basic_panels = AbstractEmailForm.content_panels + [
        SectionBase.section_content_panels,
        SectionBase.section_layout_panels,
        SectionBase.section_design_panels,
    ]

    # advanced tab panels
    advanced_panels = [
        SectionTitleBlock.title_basic_panels,
        ButtonAction.button_action_panel
    ]

    # form tab panels
    form_panels = [
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

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(basic_panels, heading="Basic"),
            ObjectList(form_panels, heading="Form"),
            ObjectList(advanced_panels, heading="Plus+"),

        ]
    )

    # Page settings
    template = 'sections/form_section_preview.html'
    parent_page_types = ['components.FormIndexPage']
    subpage_types = []

    # Overriding Methods
    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #     # Get form and update attributes
    #     # https://stackoverflow.com/questions/48321770/how-to-modify-attributes-of-the-wagtail-form-input-fields
    #     return form

    def serve(self, request):
        if request.is_ajax():
            print('IS AXJAX')
        return super(FormSection, self).serve(request)

    def __str__(self):
        if self.title:
            return self.title + " (Form Section)"
        else:
            return super(AbstractEmailForm, self).__str__()

    class Meta:
        verbose_name = 'Form Section'
        verbose_name_plural = 'Form Sections'