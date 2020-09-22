from django.conf import settings
from functools import lru_cache

DEFAULTS = {

    # Default values
    'FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT': 'navbar-light',
    'FRONTEND_NAVBAR_FORMAT_DEFAULT': '',
    'FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT': 'navbar-expand-lg',
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