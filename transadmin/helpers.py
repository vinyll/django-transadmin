from django.utils.translation import get_language
from django.db import DatabaseError
from django.core.exceptions import AppRegistryNotReady

from jingo import register

from .models import Translation


@register.function
def _(text, context=None):
    try:
        trans = Translation.objects.translate(text, get_language(), context)
        return trans.text if trans else text
    except (Translation.DoesNotExist, TypeError, DatabaseError,
            AppRegistryNotReady):
        return text


def trans(*args, **kwargs):
    return _(*args, **kwargs)
