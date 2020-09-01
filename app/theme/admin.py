# from wagtail.contrib.modeladmin.options import (
#     ModelAdmin,
#     ModelAdminGroup,
#     modeladmin_register
# )
# from theme.models import Header
# from wagtail.admin.edit_handlers import FieldPanel
# from theme.util import CustomURLHelper


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


# modeladmin_register(ThemeGroupAdmin)
