""" Content section model """
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    RichTextField, TabbedInterface, ObjectList, RichTextFieldPanel)
from wagtail.snippets.models import register_snippet

from section.sections import SectionBase


@register_snippet
class ContentSection(Page, SectionBase):
    """A content section with an WYSIWYG Richtext editro"""
    content_richtext = RichTextField()

    # basic tab panels
    basic_panels = Page.content_panels + [
        SectionBase.section_content_panels,
        RichTextFieldPanel('content_richtext', heading='Richtext', ),

        SectionBase.section_layout_panels,
        SectionBase.section_design_panels,
    ]

    # Register Tabs
    edit_handler = TabbedInterface(
        [
            ObjectList(basic_panels, heading="Basic"),
        ]
    )

    # Page settings
    template = 'sections/content_section_preview.html'
    parent_page_types = ['home.HomePage']
    subpage_types = []

    # Overring methods
    def set_url_path(self, parent):
        """
        Populate the url_path field based on this page's slug and the specified parent page.
        (We pass a parent in here, rather than retrieving it via get_parent, so that we can give
        new unsaved pages a meaningful URL when previewing them; at that point the page has not
        been assigned a position in the tree, as far as treebeard is concerned.
        """
        if parent:
            self.url_path = ''
        else:
            # a page without a parent is the tree root, which always has a url_path of '/'
            self.url_path = '/'

        return self.url_path
