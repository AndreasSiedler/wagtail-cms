from django.conf import settings
from functools import lru_cache

DEFAULTS = {


    # Form
    'FORM_FIELD_WIDTH_CHOICES_DEFAULT': 'full',
    'FORM_FIELD_WIDTH_CHOICES': (
        ('full', 'Full width'),
        ('half', 'Half width'),
        ('third', 'Third width'),
        ('quarter', 'Quarter width'),
    ),

    # Navbar
    'NAVBAR_COLOR_SCHEME_CHOICES_DEFAULT': 'light',
    'NAVBAR_COLOR_SCHEME_CHOICES': (
        ('light_basic', 'Light'),
        ('dark_basic', 'Dark'),
    ),
    'NAVBAR_LAYOUT_SCHEME_CHOICES_DEFAULT': 'light',
    'NAVBAR_LAYOUT_SCHEME_CHOICES': (
        ('light_basic', 'Light'),
        ('dark_basic', 'Dark'),
    ),

    # Button
    'BUTTON_FONT_WEIGHT_CHOICES_DEFAULT': 'font-normal',
    'BUTTON_FONT_WEIGHT_CHOICES': (
        ('font-hairline', 'Hairline'),
        ('font-thin', 'Thin'),
        ('font-light', 'Light'),
        ('font-normal', 'Default'),
        ('font-hairline', 'Hailine'),
        ('font-medium', 'Medium'),
        ('font-semibold', 'Semibold'),
        ('font-bold', 'Bold'),
        ('font-extrabold', 'Extrabold'),
        ('font-black', 'Black'),
    ),

    'BUTTON_COLOR_TYPE_CHOICES_DEFAULT': 'primary',
    'BUTTON_COLOR_TYPE_CHOICES': (
        ('primary', 'Primary Color'),
        ('secondary', 'Secondary Color'),
        ('custom', 'Custom Color'),
    ),

    'BUTTON_PADDING_COICES': (
        ('px-1 py-1', 'Small'),
        ('px-4 py-4', 'Medium'),
        ('px-8 py-8', 'Large'),
        ('px-12 py-12', 'X-Large'),
    ),

    'BUTTON_BORDER_RADIUS_COICES': (
        ('rounded-none', 'None'),
        ('rounded-sm', 'Small'),
        ('rounded-md', 'Medium'),
        ('rounded-lg', 'Large'),
        ('rounded-full', 'Full'),
    ),

    # Section
    'SECTION_COLOR_THEME_CHOICES': (
        ('light', 'Light'),
        ('dark', 'Dark'),
    ),

    'SECTION_TOP_BOTTOM_PADDING_CHOICES_DEFAULT': 'py-40',
    'SECTION_TOP_BOTTOM_PADDING_CHOICES': (
        ('py-0', 'None'),
        ('py-24', 'Small'),
        ('py-40', 'Medium'),
        ('py-56', 'Large'),
        ('py-64', 'X-Large'),
    ),

    'SECTION_CONTAINER_WIDTH_CHOICES_DEFAULT': 'container',
    'SECTION_CONTAINER_WIDTH_CHOICES': (
        ('container max-w-2xl', 'Small'),
        ('container max-w-4xl', 'Medium'),
        ('container', 'Large'),
        ('container max-w-full', 'Full'),
    ),

    # Blocks
    'TITLE_FONT_SIZE_CHOICES': (
        ('text-2xl', 'X-Small'),
        ('text-3xl', 'Small'),
        ('text-4xl', 'Medium'),
        ('text-5xl', 'Large'),
        ('text-6xl', 'X-Large'),
    ),
    'TITLE_FONT_WEIGHT_CHOICES': (
        ('font-thin', 'Thin'),
        ('font-light', 'Light'),
        ('font-normal', 'Normal'),
        ('font-medium', 'Medium'),
        ('font-bold', 'Bold'),
    ),
    # Feature
    'FEATURE_LAYOUT_CHOICES_DEFAULT': 'simple-centered',
    'FEATURE_LAYOUT_CHOICES': (
        ('simple-centered', 'Simple centered'),
    ),

    'FEATURE_COLUMN_COUNT_CHOICES_DEFAULT': 'grid-cols-3',
    'FEATURE_COLUMN_COUNT_CHOICES': (
        ('grid-cols-2', 'Two'),
        ('rid-cols-3', 'Three'),
        ('grid-cols-4', 'Four'),
    ),

}


@lru_cache()
def get_config():
    config = DEFAULTS.copy()
    for var in config:
        cr_var = 'CODERED_%s' % var
        if hasattr(settings, cr_var):
            config[var] = getattr(settings, cr_var)
    return config


cr_settings = get_config()
