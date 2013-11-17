from django import forms

from .models import Translation
from .settings import LANGUAGES, CONTEXTS


class TranslationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TranslationForm, self).__init__(*args, **kwargs)
        self.fields['context'].required = False
        self.fields['comment'].required = False
        self.fields['trans'].required = False
        if LANGUAGES:
            self.fields['language'] = forms.ChoiceField(choices=LANGUAGES)
        if CONTEXTS:
            self.fields['context'] = forms.ChoiceField(choices=CONTEXTS)

    class Meta:
        model = Translation
        exclude = ('source_uid',)
