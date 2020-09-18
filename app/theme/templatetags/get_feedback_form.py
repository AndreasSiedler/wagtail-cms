from django import template
from theme.models import Appearance

register = template.Library()


@register.simple_tag(takes_context=True)
def get_feedback_form(context):
    request = context['request']
    site_settings = Appearance.for_request(request)
    feedback_form_page = site_settings.feedback_form_page.specific
    form = feedback_form_page.get_form(
        page=feedback_form_page, user=request.user)
    return {'page': feedback_form_page, 'form': form}
