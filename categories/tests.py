from django.test import TestCase
from django.core.urlresolvers import resolve
from categories.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    
    def test_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_correct_html_returned(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>iBlog</title>' , response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
