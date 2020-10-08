""" Section Model """
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from django.http import JsonResponse

from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailmetadata.models import MetadataPageMixin

from section.sections import (
    FeatureSection, HeroSection, FormSection, SubscriptionSection, ContentSection)


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
                'content_section',
                SnippetChooserBlock(
                    ContentSection,
                    icon='list-ul',
                    template='sections/content_section.html'
                )
            ),
            (
                'form_section',
                SnippetChooserBlock(
                    FormSection,
                    icon='list-ul',
                    template='sections/form_section.html',
                    can_choose_root=False
                )
            ),
            (
                'subscription_section',
                SnippetChooserBlock(
                    SubscriptionSection,
                    icon='list-ul',
                    template='sections/subscription_section.html',
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

    def serve(self, request):
        """
        Here you can catch ajax request for the section page
        HINT: We dont use Routable Page Mixin because you can just make read only get requests - Just read only - you cant make an post request!
        """
        if request.is_ajax():
            # Check request type via query params
            request_type = request.GET.get('type', 'default')

            # FORM SECTION SUBMIT
            if request.method == 'POST' and request_type == 'submit-form':
                fs = FormSection.objects.get(pk=request.POST['id'])
                form = fs.get_form(request.POST, request.FILES,
                                   page=fs, user=request.user)

                if form.is_valid():
                    form_submission = fs.process_form_submission(form)
                    return JsonResponse({'success': True})
                else:
                    return JsonResponse({'success': False,
                                         'errors': form.errors}, status=400)

            # CATCH HER FURTHER AJAX REQUESTS

        return super(SectionPage, self).serve(request)

    class Meta:
        verbose_name = 'Section Page'
        verbose_name_plural = 'Section Pages'
