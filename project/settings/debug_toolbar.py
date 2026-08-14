from .installed_apps import INSTALLED_APPS
from .middlewares import MIDDLEWARE
from .enviroment import DEBUG


if DEBUG:
    INSTALLED_APPS += ['debug_toolbar',]

    MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']

    # django debug tool bar
    INTERNAL_IPS = [
        # ...
        "127.0.0.1",
        # ...
    ]