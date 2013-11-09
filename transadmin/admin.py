from django.contrib import admin
from django import forms

from .models import Translation
from .forms import TranslationForm


class TranslationAdmin(admin.ModelAdmin):
    model = Translation
    form = TranslationForm
    list_display = ('source', 'context', 'language', 'trans_summary',)
    list_filter = ('context', 'language',)


admin.site.register(Translation, TranslationAdmin)
