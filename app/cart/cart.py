from django.contrib.sessions.backends.db import SessionStore

from django.conf import settings

from .forms import CartForm
from app.product.models import Product


class Cart:

    def __init__(self, session):
        self.session = session
        self.cart = session.get(settings.CART_SESSION_ID)
        if not self.cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}

    def __iter__(self):
        products = Product.objects.filter(id__in=self.cart.keys())

        for product in products:
            self.cart[str(product.id)]['object'] = product

        for item_id, data in self.cart.items():
            data['total_price'] = round(data['quantity'] * data['object'].price, 2)
            # self.total += data['total_price']
            yield data

    def __len__(self):
        return len(self.cart)

    def __getitem__(self, item):
        return self.cart[str(item)]

    def is_empty(self):
        return len(self.cart) == 0

    def add(self, product_id, quantity=1, update=False):
        product_id = str(product_id)
        if product_id in self.cart and not update:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart.update({str(product_id):{'quantity':quantity}})
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart.pop(product_id)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def total_sum(self):
        total = 0
        for item in self:
            total += item['total_price']
        return float(round(total, 2))

    def prepare_to_render(self, update):
        for item in self:
            form_initial = {
                'quantity': item['quantity'],
                'update': update
            }
            item['cartadd_form'] = CartForm(initial=form_initial)