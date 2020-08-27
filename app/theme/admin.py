from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from theme.models import Header
from wagtail.admin.edit_handlers import FieldPanel


class ThemeHeaderModelAdmin(ModelAdmin):
    model = Header
    menu_label = "Header"
    panels = [
        FieldPanel('color'),
    ]


# Register your models here.
class ThemeGroupAdmin(ModelAdminGroup):
    menu_label = "Theme"
    menu_order = 100
    items = [
        ThemeHeaderModelAdmin
    ]


modeladmin_register(ThemeGroupAdmin)
