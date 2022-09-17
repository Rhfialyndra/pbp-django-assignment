from django.test import TestCase
from django.urls import reverse  


# Create your tests here.

# unit test:

class CatalogTests(TestCase):
    def test_current_url_is_correct(self):
        resp = self.client.get("/katalog/")
        self.assertEqual(resp.status_code, 200)

    def test_url_corresponding_name(self):  
        resp = self.client.get(reverse("katalog:show_catalog"))
        self.assertEqual(resp.status_code, 200)

    def test_template(self):  
        resp = self.client.get(reverse("katalog:show_catalog"))
        self.assertTemplateUsed(resp, "katalog.html")