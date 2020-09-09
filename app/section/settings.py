from django.conf import settings
from functools import lru_cache

DEFAULTS = {

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