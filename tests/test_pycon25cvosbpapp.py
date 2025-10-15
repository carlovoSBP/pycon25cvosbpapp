from unittest import TestCase

from pycon25cvosbpapp import app_hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello app from pycon25cvosbp!", app_hello())
