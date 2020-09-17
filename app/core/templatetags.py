from django import template
from myapp.models import MyCustomSettings

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.assignment_tag(takes_context=True)
def get_feedback_form(context):
    request = context['request']
    # my_custom_settings = MyCustomSettings.for_site(request.site)
    feedback_form_page = my_custom_settings.feedback_form_page.specific
    form = feedback_form_page.get_form(
        page=feedback_form_page, user=request.user)
    return {'page': feedback_form_page, 'form': form}