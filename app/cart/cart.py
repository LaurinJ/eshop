from django.contrib.sessions.backends.db import SessionStore

from django.conf import settings

from app.product.models import Product


class Cart:

    def __init__(self, session):
        self.session = session
        self.cart = session.get(settings.CART_SESSION_ID)
        self.total = 1
        if not self.cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}

    def __iter__(self):
        products = Product.objects.filter(id__in=self.cart.keys())

        for product in products:
            self.cart[str(product.id)]['object'] = product

        for item_id, data in self.cart.items():
            data['total_price'] = data['quantity'] * data['object'].price
            self.total += data['total_price']
            yield data

    def __len__(self):
        return len(self.cart)

    def __getitem__(self, item):
        return self.cart[str(item)]

    def is_empty(self):
        return len(self.cart) == 0

    def add(self, product_id, quantity=1):
        self.cart.update({str(product_id):{'quantity':quantity}})
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True