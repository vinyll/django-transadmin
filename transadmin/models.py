from django.db import models
from django.conf import settings


class TranslationManager(models.Manager):
    def translate(self, text, lang, context=None, source_lang=None):
        return self.get(#models.Q(context=context) | models.Q(context=None),
                        source_lang=source_lang or settings.LANGUAGE_CODE,
                        source_text=text,
                        target_lang=lang)


class Translation(models.Model):
    context = models.CharField(max_length=50, null=True)
    source_lang = models.CharField(max_length=5, null=False,
                                   default=settings.LANGUAGE_CODE)
    target_lang = models.CharField(max_length=5, null=False,
                                   default=settings.LANGUAGE_CODE,
                                   choices=getattr(settings, 'LANGUAGES'))
    source_text = models.TextField(null=False)
    target_text = models.TextField()

    objects = TranslationManager()

    @property
    def text(self):
        return self.target_text

    def __unicode__(self):
        return u"%s %s>%s \"%s\"" % (self.context or "[no context]",
                                     self.source_lang,
                                     self.target_lang, self.source_text)

    class Meta:
        unique_together = ('context', 'source_lang', 'source_text')
