VERSION = (2, 4, 2)
__version__ = '.'.join(map(str, VERSION if VERSION[-1] else VERSION[:2]))


from django.apps import AppConfig
from django.conf import settings


FAKE = getattr(settings, 'CACHEOPS_FAKE', False)
if not FAKE:
    from .simple import *
    from .query import *
    from .invalidation import *
    from .templatetags.cacheops import *
    from .transaction import install_cacheops_transaction_support
else:
    from .fake import *


class CacheopsConfig(AppConfig):
    name = 'cacheops'

    def ready(self):
        install_cacheops()
        install_cacheops_transaction_support()

default_app_config = 'cacheops.CacheopsConfig'
