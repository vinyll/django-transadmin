from django.test import TestCase

from .models import Translation
from .helpers import _


def create_translation():
    return (Translation.objects.create(source_lang='en',
                                       target_lang='fr',
                                       source_text="Test me!",
                                       target_text="Testez-moi !"),
            Translation.objects.create(source_lang='en',
                                       target_lang='fr',
                                       source_text="Test me!",
                                       target_text="Essayez-moi !",
                                       context="shopping")
            )


class ModelTest(TestCase):
    def setUp(self):
        self.trans, self.trans2 = create_translation()

    def test_translate(self):
        self.assertEqual(
            Translation.objects.translate("Test me!", 'fr')[0].text,
            "Testez-moi !")

    def test_context(self):
        self.assertEqual(
            Translation.objects.translate("Test me!", 'fr',
                                          context='shopping')[0].text,
            "Essayez-moi !")

class HelperTest(TestCase):
    def setUp(self):
        Translation.objects.create(source_lang='en',
                                   target_lang='en',
                                   source_text="Test me!",
                                   target_text="Test me translated!")

    def test_underscore(self):
        self.assertEqual(_("Test me!"), "Test me translated!")

    def test_not_found(self):
        self.assertTrue(_("Test me!", 'de'), "Test me!")
