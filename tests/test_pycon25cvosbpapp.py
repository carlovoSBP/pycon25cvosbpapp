from unittest import TestCase

from pycon25cvosbpapp import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello you from pycon25cvosbpapp!", hello())
