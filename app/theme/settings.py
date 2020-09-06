from django.conf import settings
from functools import lru_cache

DEFAULTS = {

    # Default values
    'FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT': 'navbar-light',
    'FRONTEND_NAVBAR_FORMAT_DEFAULT': '',
    'FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT': 'navbar-expand-lg',

    # Navbar
    'FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES': (
        ('navbar-light', 'Light - for use with a light-colored navbar'),
        ('navbar-dark', 'Dark - for use with a dark-colored navbar'),
    ),

    'FRONTEND_NAVBAR_FORMAT_CHOICES': (
        ('', 'Default Bootstrap Navbar'),
        ('codered-navbar-center', 'Centered logo at top'),
    ),

    'FRONTEND_NAVBAR_COLLAPSE_MODE_CHOICES': (
        ('', 'Never show menu - Always collapse menu behind a button'),
        ('navbar-expand-sm', 'sm - Show on small screens (phone size) and larger'),
        ('navbar-expand-md', 'md - Show on medium screens (tablet size) and larger'),
        ('navbar-expand-lg', 'lg - Show on large screens (laptop size) and larger'),
        ('navbar-expand-xl', 'xl - Show on extra large screens (desktop, wide monitor)'),
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

    'BUTTON_PADDING_COICES_DEFAULT': 'px-2 py-2',
    'BUTTON_PADDING_COICES': (
        ('px-2 py-2', 'Default'),
        ('px-1 py-1', 'Small'),
        ('px-4 py-4', 'Medium'),
        ('px-8 py-8', 'Large'),
        ('px-12 py-12', 'X-Large'),
    ),
    
    'BUTTON_BORDER_RADIUS_COICES_DEFAULT': 'rounded',
    'BUTTON_BORDER_RADIUS_COICES': (
        ('rounded', 'Default'),
        ('rounded-none', 'None'),
        ('rounded-sm', 'Small'),
        ('rounded-md', 'Medium'),
        ('rounded-lg', 'Large'),
        ('rounded-full', 'Full'),
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