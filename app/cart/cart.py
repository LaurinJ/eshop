from django.contrib.sessions.backends.db import SessionStore

from django.conf import settings

class Cart:

    def __init__(self, session):
        self.session = session
        self.cart = session.get(settings.CART_SESSION_ID)
        if not self.cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}

    def __getitem__(self, item):
        return self.cart[item]

    def is_empty(self):
        return len(self.cart) == 0

    def add(self, product_id, quantity=1):
        self.cart.update({str(product_id):quantity})