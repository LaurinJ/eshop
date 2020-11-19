from unittest import skip

from django.test import TestCase
from django.urls import resolve, reverse

from ..views import CartDetailView

class CartDetailViewTest(TestCase):

    def test_cart_detail_url_resolves_to_cart_detail_view(self):
        page = resolve(reverse('cart:detail'))
        self.assertEqual(page.func.__name__, CartDetailView.__name__)

    def test_detail_shows_no_items_when_empty(self):
        response = self.client.get(reverse('cart:detail'))
        self.assertIn(b'The cart is empty', response.content)

    @skip
    def test_cart_detail_shows_items_when_not_emtpy(self):
        pass