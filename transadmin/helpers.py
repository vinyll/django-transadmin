from jingo import register

from django.utils.translation import get_language

from .models import Translation


@register.function
def _(text, source_lang=None, context=None):
    try:
        trans = Translation.objects.translate(text, get_language(), context,
                                              source_lang)
        return trans.text
    except Translation.DoesNotExist:
        return text


def trans(*args, **kwargs):
    return _(*args, **kwargs)
