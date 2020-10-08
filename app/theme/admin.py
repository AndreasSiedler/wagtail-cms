from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Appearance
# from theme.models import Header
# from wagtail.admin.edit_handlers import FieldPanel
from theme.util import CustomURLHelper

class ThemeAdmin(ModelAdmin):
    """
    Create ThemeAdmin instance to use it for the url_helper - REVERSING
    If you want to hide it from the menu admin bar exclude it in the hooks section with the intace type
    """
    model = Appearance

# class ThemeHeaderModelAdmin(ModelAdmin):
#     model = Header
#     menu_label = "Header"
#     panels = [
#         FieldPanel('color'),
#     ]
#     add_to_settings_menu = False
#     exclude_from_explorer = True
#     url_helper_class = CustomURLHelper

#     # def get_queryset(self, request):
#     #     qs = super().get_queryset(request)
#     #     return qs.filter(color="blau")


# # Register your models here.
# class ThemeGroupAdmin(ModelAdminGroup):
#     menu_label = "Theme"
#     menu_order = 100
#     items = [
#         ThemeHeaderModelAdmin
#     ]


modeladmin_register(ThemeAdmin)
