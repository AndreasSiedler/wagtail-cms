from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from section.sections import (
    HeroSection, FeatureSection, SubscriptionSection)
from .sections import FormIndexPage, FormSection
from section.models import SectionPage


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


class SubscriptionSectionModelAdmin(ModelAdmin):
    model = SubscriptionSection
    menu_label = "Subscription Sections"
    add_to_settings_menu = False
    exclude_from_explorer = True


class FormSectionModelAdmin(ModelAdmin):
    model = FormSection
    menu_label = "Forms"
    add_to_settings_menu = False
    exclude_from_explorer = True
    # panels = [
    #     FieldPanel('color'),
    # ]

    # url_helper_class = CustomURLHelper

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(color="blau")


# @modeladmin_register
# class SectionsModelAdmin(ModelAdmin):
#     model = SectionPage
#     menu_label = "Sections"
#     add_to_settings_menu = False
#     exclude_from_explorer = True
#     # panels = [
#     #     FieldPanel('color'),
#     # ]

#     # url_helper_class = CustomURLHelper
#         # Schau dir django reverse querying von JSONfields an
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.filter(color="blau")


# Register your models here.
class ComponentsGroupAdmin(ModelAdminGroup):
    menu_label = "Components"
    menu_order = 100
    menu_icon = "placeholder"
    items = [
        FormSectionModelAdmin,
        HeroSectionModelAdmin,
        FeatureSectionModelAdmin,
        SubscriptionSectionModelAdmin,
    ]


modeladmin_register(ComponentsGroupAdmin)
