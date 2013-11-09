from django.db import models
from django.dispatch import receiver


class TranslationManager(models.Manager):
    def translate(self, source, language, context=None):
        trans = self.filter(source=source, language=language)
        if context:
            trans = trans.filter(context=context)
        return trans


class Translation(models.Model):
    context = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=5, null=False)
    source = models.TextField(null=False)
    trans = models.TextField(null=True)
    comment = models.TextField(null=True)

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
        unique_together = ('context', 'language', 'source')


@receiver(models.signals.pre_save, sender=Translation)
def translation_empty_context(sender, instance, **kwargs):
    if instance.context == "":
        instance.context = None
