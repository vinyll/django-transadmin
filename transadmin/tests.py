from django.test import TestCase

from .models import Translation
from .helpers import _


def create_translation():
    return Translation.objects.create(source_lang='en',
                                      target_lang='fr',
                                      source_text="Test me!",
                                      target_text="Testez-moi !")


class ModelTest(TestCase):
    def setUp(self):
        self.trans = create_translation()

    def test_translate(self):
        self.assertEqual(Translation.objects.translate("Test me!", 'fr').text,
                         "Testez-moi !")


class HelperTest(TestCase):
    def setUp(self):
        Translation.objects.create(source_lang='en',
                                   target_lang='en',
                                   source_text="Test me!",
                                   target_text="Test me translated!")

    def test_underscore(self):
        self.assertTrue(_("Test me!", "Test me translated!"))
