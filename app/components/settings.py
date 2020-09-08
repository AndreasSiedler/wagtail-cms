from django.conf import settings
from functools import lru_cache

DEFAULTS = {

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