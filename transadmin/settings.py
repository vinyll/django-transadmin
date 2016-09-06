from django.conf import settings


CONTEXTS = getattr(settings, 'TRANSADMIN_CONTEXTS', None)
LANGUAGES = getattr(settings, 'TRANSADMIN_LANGUAGES',
                    getattr(settings, 'LANGUAGES'))
FALLBACK_LANGUAGE = getattr(settings, 'TRANSADMIN_FALLBACK_LANGUAGE', None)
