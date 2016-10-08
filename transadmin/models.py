import hashlib

from django.db import models
from django.dispatch import receiver
from .settings import FALLBACK_LANGUAGE


class TranslationManager(models.Manager):
    def translate(self, source, language, context=None,
                  fallback=FALLBACK_LANGUAGE):
        """
        Find the translation for a language. If it is not found it will take
        the one with the fallback language.
        """

        if not fallback or language == fallback:
            try:
                return self.filter(source=source, language=language)[0]
            except IndexError:
                return None

        q = ('select *, case language when %(lang)s then 1 when %(fallback)s '
             'then 2 else 3 end as score from transadmin_translation where '
             'source = %(source)s order by score limit 1')
        params = {'source': source, 'lang': language, 'fallback': fallback}
        try:
            return list(Translation.objects.raw(q, params))[0]
        except IndexError:
            return None


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
