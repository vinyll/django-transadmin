from django.conf import settings


CONTEXTS = getattr(settings, 'TRANSADMIN_CONTEXTS', None)
LANGUAGES = getattr(settings, 'TRANSADMIN_LANGUAGES',
                    getattr(settings, 'LANGUAGES'))
