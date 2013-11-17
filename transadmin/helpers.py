from django.utils.translation import get_language
from django.db import DatabaseError

from jingo import register

from .models import Translation


@register.function
def _(text, context=None):
    try:
        trans = Translation.objects.translate(text, get_language(), context)
        translated = trans[0].text
        return translated or text
    except (Translation.DoesNotExist, IndexError, TypeError, DatabaseError):
        return text


def trans(*args, **kwargs):
    return _(*args, **kwargs)
