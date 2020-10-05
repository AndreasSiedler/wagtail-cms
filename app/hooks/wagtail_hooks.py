# from django.templatetags.static import static
# from django.utils.html import format_html
# from django.utils.safestring import mark_safe

from wagtail.core import hooks
from section.admin import FormSectionModelAdmin, FormSection
from django.shortcuts import redirect
from wagtail.snippets.wagtail_hooks import SnippetsMenuItem
from wagtail.contrib.modeladmin.menus import ModelAdminMenuItem
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from theme.admin import ThemeAdmin
from theme.models import Appearance


@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
    """
    Use the admin instance url helper to create the url
    """
    url_helper = ThemeAdmin().url_helper
    index_url = url_helper.get_action_url('edit', 1)
    return MenuItem('Appearance', index_url, icon_name='snippet', order=10000)


class WelcomePanel:
    order = 50

    def render(self):
        return mark_safe("""
        <section class="panel summary nice-padding">
          <h3>No, but seriously -- welcome to the admin homepage.Please change your global design!</h3> 
        </section>
        """)


@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.append(WelcomePanel())


@hooks.register('construct_page_listing_buttons')
def remove_page_listing_button_item(buttons, page, page_perms, is_parent=False, context=None):
    if is_parent:
        buttons.pop()


@hooks.register('after_publish_page')
def after_publish_page(request, page_class):
    # Use a custom create view for the AwesomePage model
    if type(page_class) == FormSection:
        url_helper = FormSectionModelAdmin().url_helper
        index_url = url_helper.get_action_url('index')
        return redirect(index_url)


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    """
    Loop throug the admin menu items and hide via defining the instace type or the label or etc.
    Use the debug launcher for it
    """
    menu_items[:] = [item for item in menu_items if not isinstance(
        item, ModelAdminMenuItem) and not isinstance(item, SnippetsMenuItem)]


# @hooks.register('insert_editor_css')
# def editor_css():
#     return format_html(
#         '<link rel="stylesheet" href="{}">',
#         static('css/custom-editor.css')
#     )

# @hooks.register('insert_editor_js', order=100)
# def editor_js():
#     return format_html(
#         '<script src="{}"></script>',
#         static('js/custom-editor.js')
#     )

# @hooks.register("insert_global_admin_css", order=100)
# def global_admin_css():
#     """Add /static/css/custom.css to the admin."""
#     return format_html(
#         '<link rel="stylesheet" href="{}">',
#         static("css/custom.css")
#     )

# @hooks.register("insert_global_admin_js", order=100)
# def global_admin_js():
#     """Add /static/css/custom.js to the admin."""
#     return format_html(
#         '<script src="{}"></script>',
#         static("/js/custom.js")
#     )