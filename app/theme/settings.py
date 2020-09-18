from django.conf import settings
from functools import lru_cache

DEFAULTS = {

    # Default values
    'FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT': 'navbar-light',
    'FRONTEND_NAVBAR_FORMAT_DEFAULT': '',
    'FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT': 'navbar-expand-lg',

    # Navbar
    'FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES': (
        ('light_basic', 'Light'),
        ('dark_basic', 'Dark'),
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