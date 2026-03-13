from django.test import SimpleTestCase

class SimpleMathTest(SimpleTestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)