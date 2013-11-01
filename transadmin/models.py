from django.db import models
from django.conf import settings


class TranslationManager(models.Manager):
    def translate(self, text, lang, context=None, source_lang=None):
        trans = self.filter(source_text=text,
                            target_lang=lang)
        if source_lang:
            trans = trans.filter(source_lang=source_lang)
        if context:
            trans = trans.filter(context=context)
        return trans


class Translation(models.Model):
    context = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=5, null=False,
                                default=settings.LANGUAGE_CODE,
                                choices=getattr(settings, 'LANGUAGES'))
    source = models.TextField(null=False)
    trans = models.TextField(null=True)
    comment = models.TextField(null=True)


    @property
    def is_translated(self):
        return self.trans != "" and self.trans is not None

    objects = TranslationManager()

    @property
    def text(self):
        return self.target_text

    def __unicode__(self):
        return u"%s(%s) \"%s\"" % (self.context or "[no context]",
                                     self.language, self.source)

    class Meta:
        unique_together = ('context', 'language', 'source')
