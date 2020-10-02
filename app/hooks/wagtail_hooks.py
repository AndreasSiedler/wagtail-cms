# from django.templatetags.static import static
# from django.utils.html import format_html
# from django.utils.safestring import mark_safe

from wagtail.core import hooks
from section.admin import FormSectionModelAdmin, FormSection
from django.shortcuts import redirect
from wagtail.snippets.wagtail_hooks import SnippetsMenuItem
from django.http import HttpResponse


@hooks.register('before_edit_snippet')
def block_snippet_edit(request, instance):
    if isinstance(instance) and instance.prevent_edit:
        print('Edit Snippet')


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


@hooks.register('construct_explorer_page_queryset')
def dont_show_index_pages(parent_page, pages, request):
    # If we're in the 'user-profiles' section, only show the user's own profile
    print(pages)

    return pages


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if not isinstance(item, SnippetsMenuItem)]


# @hooks.register("construct_main_menu")
# def change_snippet_name(request, menu_items):
#     for item in menu_items:
#         if item.__class__.__name__ == "SnippetsMenuItem":
#             item.label = "Sections & Blocks"


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


# class WelcomePanel:
#     order = 110

#     def render(self):
#         return mark_safe("""
#         <section class="panel summary nice-padding">
#           <h3>Dashboard Panel Section Title</h3>
#           <button data-modal-trigger="some-param">Open Modal</button>
#         </section>
#         """)

# @hooks.register('construct_homepage_panels')
# def add_another_welcome_panel(request, panels):
#     panels.append(WelcomePanel())