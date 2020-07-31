from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from wagtail.core import hooks

@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/custom-editor.css')
    )

@hooks.register('insert_editor_js', order=100)
def editor_js():
    return format_html(
        '<script src="{}"></script>',
        static('js/custom-editor.js')
    )

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