from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from components.sections import HeroSection, FeatureSection
from .models import FormSection, FormIndexPage


class HeroSectionModelAdmin(ModelAdmin):
    model = HeroSection
    menu_label = "Hero Sections"
    add_to_settings_menu = False
    exclude_from_explorer = True


class FeatureSectionModelAdmin(ModelAdmin):
    model = FeatureSection
    menu_label = "Feature Sections"
    add_to_settings_menu = False
    exclude_from_explorer = True


@modeladmin_register
class FormIndexPageModelAdmin(ModelAdmin):
    model = FormIndexPage
    add_to_settings_menu = False
    exclude_from_explorer = True


class FormSectionModelAdmin(ModelAdmin):
    model = FormSection
    menu_label = "Forms"
    # panels = [
    #     FieldPanel('color'),
    # ]
    add_to_settings_menu = False
    exclude_from_explorer = True
    # url_helper_class = CustomURLHelper

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(color="blau")


# Register your models here.
class ComponentsGroupAdmin(ModelAdminGroup):
    menu_label = "Components"
    menu_order = 100
    menu_icon = "placeholder"
    items = [
        FormSectionModelAdmin,
        HeroSectionModelAdmin,
        FeatureSectionModelAdmin
    ]


modeladmin_register(ComponentsGroupAdmin)
