from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel, MultiFieldPanel


class Footer(models.Model):
    feedback_form_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)
    # Panels
    # footer_panel = MultiFieldPanel(
    #     [
    #         PageChooserPanel('feedback_form_page', ['section.FormSection']),
    #     ],
    #     heading='Footer',
    #     classname='collapsible',
    #     help_text="A call to action button (CTA), depending on the situation, will usually prompt users to sign up/register/buy now/etc. CTA buttons should be used where the platform wants to strongly suggest something that the user should do."
    # )

    class Meta:
        abstract = True
