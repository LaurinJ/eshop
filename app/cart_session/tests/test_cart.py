from django.contrib.sessions.backends.db import SessionStore
from django.test import TestCase
from django.conf import settings

from ..cart import Cart


class CartTest(TestCase):

    def setUp(self):
        self.session = SessionStore()
        self.cart = Cart(self.session)

    def test_create_cart(self):
        self.assertTrue(hasattr(self.cart, 'session'))
        self.assertIsInstance(self.cart.session, SessionStore)
        self.assertTrue(hasattr(self.cart, 'cart'))
        self.assertIsInstance(self.cart.cart, dict)

    def test_new_cart_is_empty(self):

        self.assertTrue(self.cart.is_empty())

    def test_cart_add_item(self):
        product_id = '2'
        quantity = 1
        self.cart.add(product_id=product_id, quantity=quantity)

        self.assertEqual(self.cart[product_id], quantity)

    def test_add_cart_updates_session(self):
        product_id = '2'
        quantity = 1
        self.cart.add(product_id=product_id, quantity=quantity)

        self.assertEqual(self.session[settings.CART_SESSION_ID][product_id], self.cart[product_id])