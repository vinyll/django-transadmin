import hashlib

from django.db import models
from django.dispatch import receiver
from .settings import FALLBACK_LANGUAGE


# Cached queries
_translated = {}


class TranslationManager(models.Manager):
    def translate(self, source, language, context=None,
                  fallback=FALLBACK_LANGUAGE):
        """
        Find the translation for a language. If it is not found it will take
        the one with the fallback language.
        """
        params = {'source': source, 'lang': language, 'fallback': fallback}
        cache_key = '|'.join(params.values())
        if cache_key in _translated:
            return _translated[cache_key]

        if not fallback or language == fallback:
            _translated[cache_key] = self.filter(source=source,
                                                 language=language)[0]
        else:
            q = ('select *, case language when %(lang)s then 1 when '
                 '%(fallback)s then 2 else 3 end as score from '
                 'transadmin_translation where source = %(source)s '
                 'order by score limit 1')
            if cache_key not in _translated:
                _translated[cache_key] = list(
                    Translation.objects.raw(q, params))[0]
        return _translated[cache_key]

    def for_language(self, language, fallback=FALLBACK_LANGUAGE):
        if not fallback or language == fallback:
            return self.filter(language=language)
        q = ('select *, case language when %(lang)s then 1 when %(fallback)s '
             'then 2 else 3 end as score from transadmin_translation '
             'group by source order by score')
        return self.raw(q, {'lang': language, 'fallback': fallback})


class Translation(models.Model):
    context = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=5, null=False)
    source = models.TextField(null=False)
    trans = models.TextField(null=True)
    comment = models.TextField(null=True)
    # Some DB can't manage uniqueess on TextField's
    source_uid = models.CharField(max_length=32, null=True)

    @property
    def is_translated(self):
        return self.trans != "" and self.trans is not None

    @property
    def trans_summary(self):
        if self.is_translated:
            summary = self.trans[:100]
            if len(self.trans) > 100:
                summary += "..."
            return unicode(summary)
        return ""

    objects = TranslationManager()

    @property
    def text(self):
        return self.trans

    def __unicode__(self):
        return u"%s(%s) \"%s\"" % (self.context or "[no context]",
                                   self.language, self.source)

    class Meta:
        unique_together = ('context', 'language', 'source_uid')


@receiver(models.signals.pre_save, sender=Translation)
def translation_empty_context(sender, instance, **kwargs):
    if instance.context == "":
        instance.context = None


@receiver(models.signals.pre_save, sender=Translation)
def translation_generate_source_uid(sender, instance, **kwargs):
    if instance.source:
        hash = hashlib.md5()
        try:
            hash.update(instance.source.encode('utf8'))
        except UnicodeDecodeError:
            hash.update(instance.source)
        instance.uid = hash.hexdigest()
