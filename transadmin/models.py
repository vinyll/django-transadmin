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
    source_lang = models.CharField(max_length=5, null=False,
                                   default=settings.LANGUAGE_CODE)
    target_lang = models.CharField(max_length=5, null=False,
                                   default=settings.LANGUAGE_CODE,
                                   choices=getattr(settings, 'LANGUAGES'))
    source_text = models.TextField(null=False)
    target_text = models.TextField()

    @property
    def is_translated(self):
        return self.target_text != "" and self.target_text is not None

    objects = TranslationManager()

    @property
    def text(self):
        return self.target_text

    def __unicode__(self):
        return u"%s %s>%s \"%s\"" % (self.context or "[no context]",
                                     self.source_lang,
                                     self.target_lang, self.source_text)

    class Meta:
        unique_together = ('context', 'target_lang', 'source_text')
