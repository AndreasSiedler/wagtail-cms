from .base import *

DEBUG = False
SECRET_KEY = 't-zl$)!^dhh$kiz8-)!rr02t8uhn4%v6nl*f*y62p9xmxy94dh'

try:
    from .local import *
except ImportError:
    pass
