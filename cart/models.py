from django.db import models
from django.conf import settings
from django.utils import timezone
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes.fields import GenericForeignKey   #for now i guess

from shop.models import Product


class Cart(models.Model):
    created = models.DateTimeField(default=timezone.now)
    checked_out = models.BooleanField(default=False)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        if self.checked_out:
            return f'{self.pk} {self.buyer}\'s cart checked_out'
        return f'{self.pk} {self.buyer}\'s cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    #unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    #generic relation for cart item


    # TODO: fuck go back


    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #object_id = models.PositiveIntegerField()
    #content_object = GenericForeignKey()   #that's cool and all but let's try sth dumber
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # coz what could possibly go wrong

    def item_price(self):
        print('\n\n', self.quantity, '\n\n')
        return self.product.price * self.quantity
    total_price = property(item_price)

    #def get_item(self):
    #    return self.content_type.get_object_for_this_type(pk=self.object_id)

    #def set_item(self, item):
    #    self.content_type = ContentType.objects.get_for_model(type(item))
    #    self.object_id = item.pk
    #product = property(get_item, set_item)
