from django.db import models
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, blank=True)
    colourway = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    release_year = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)
    is_sale = models.BooleanField(default=False, null=True, blank=True)
    is_new = models.BooleanField(default=False, null=True, blank=True)

    def get_sale_price(self):
        if self.is_sale and hasattr(settings, 'UNIVERSAL_DISCOUNT_PERCENTAGE'):
            universal_discount = Decimal(
                settings.UNIVERSAL_DISCOUNT_PERCENTAGE)
            discount_multiplier = (
                Decimal('1.0') - universal_discount / Decimal('100.0'))
            discounted_price = self.price * discount_multiplier
            return discounted_price.quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP)
        return self.price

    def __str__(self):
        return self.name
