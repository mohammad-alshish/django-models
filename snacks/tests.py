from django.test import TestCase
from django.urls import reverse


class SnackTests(TestCase):
    # status code
    def test_snack_list_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # test templates
    def test_snack_list_temp(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_list_base_temp(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')