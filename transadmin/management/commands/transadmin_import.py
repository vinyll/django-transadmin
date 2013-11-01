from django.db import IntegrityError

try:
    import polib
except ImportError:
    raise ImportError("Transadmin commands require polib. You can install it "
                      "running: pip install polib")

from transadmin.models import Translation

from django.core.management.base import LabelCommand, make_option, CommandError


def save(source, trans, language, context=None):
    try:
        Translation.objects.get_or_create(source=source,
                                          trans=trans,
                                          language=language,
                                          context=context)
    except IntegrityError:
        pass


def extract_translations(file, language, context):
    for entry in polib.pofile(file):
        save(entry.msgid, entry.msgstr, language=language, context=context)


class Command(LabelCommand):
    label = 'po file path'
    option_list = LabelCommand.option_list + (
        make_option('-l', '--language',
            action='store', dest='language', default=None,
            help='Set the target language'),
        make_option('-c', '--context',
            action='store', dest='context', default=None,
            help='Set the context (e.g. the app name)'),
        )

    def handle_label(self, label, **options):
        language = options.get('language')
        if not language:
          raise CommandError("The -l or --language argument is required")
        extract_translations(label, options.get('language'),
                             options.get('context'))
