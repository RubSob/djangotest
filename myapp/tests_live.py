from django.test import LiveServerTestCase
import urllib.request

class SiteLiveTest(LiveServerTestCase):
    def test_server_is_up(self):
        response = urllib.request.urlopen(self.live_server_url + "/")
        self.assertEqual(response.getcode(), 200)