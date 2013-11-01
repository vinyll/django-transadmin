from django.test import TestCase

from .models import Translation
from .helpers import _


def create_translation():
    return (Translation.objects.create(language='fr',
                                       source="Test me!",
                                       trans="Testez-moi !"),
            Translation.objects.create(language='fr',
                                       source="Test me!",
                                       trans="Essayez-moi !",
                                       context="shopping")
            )


class ModelTest(TestCase):
    def setUp(self):
        self.trans, self.trans2 = create_translation()

    def test_translate(self):
        self.assertEqual(
            Translation.objects.translate("Test me!", 'fr')[0].trans,
            "Testez-moi !")

    def test_context(self):
        self.assertEqual(
            Translation.objects.translate("Test me!", 'fr',
                                          context='shopping')[0].trans,
            "Essayez-moi !")


class HelperTest(TestCase):
    def setUp(self):
        Translation.objects.create(language='en',
                                   source="Test me!",
                                   trans="Test me translated!")
        Translation.objects.create(language='en',
                                   source="Untranslated text",
                                   trans="")

    def test_underscore(self):
        self.assertEqual(_("Test me!"), "Test me translated!")

    def test_not_found(self):
        self.assertEqual(_("Test me!", 'de'), "Test me!")

    def test_blank(self):
        self.assertEqual(_("Untranslated text"), "Untranslated text")
