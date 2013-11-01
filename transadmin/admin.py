from django.contrib import admin
from django import forms

from .models import Translation


class TranslationAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TranslationAdminForm, self).__init__(*args, **kwargs)
        self.fields['context'].required = False

    class Meta:
        model = Translation


class TranslationAdmin(admin.ModelAdmin):
    model = Translation
    form = TranslationAdminForm
    list_display = ('source', 'context', 'language', 'is_translated',)
    list_filter = ('context', 'trans',)


admin.site.register(Translation, TranslationAdmin)
