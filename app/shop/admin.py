from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from shop.models import Store, Product


class ShopStoreModelAdmin(ModelAdmin):
    model = Store
    menu_label = "Stores"
    menu_icon = "fa-book"


class ShopProductModelAdmin(ModelAdmin):
    model = Product
    menu_label = "Products"
    add_to_settings_menu = True  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view


# Register your models here.
class ShopGroup(ModelAdminGroup):
    menu_label = "Shop"
    menu_icon = "fa-book"
    menu_order = 100
    items = [
        ShopStoreModelAdmin,
        ShopProductModelAdmin
    ]


modeladmin_register(ShopGroup)
