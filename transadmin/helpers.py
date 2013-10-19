from jingo import register

from django.utils.translation import get_language

from .models import Translation


@register.function
def _(text, source_lang=None, context=None):
    try:
        trans = Translation.objects.translate(text, get_language(), context,
                                              source_lang)
        translated = trans[0].text
        return translated or text
    except (Translation.DoesNotExist, IndexError):
        return text


def trans(*args, **kwargs):
    return _(*args, **kwargs)
