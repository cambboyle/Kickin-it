"""
Signals for updating order totals in the checkout app.
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order total and grand total
    when a new line item is added/updated.
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the order total and grand total
    when a new line item is deleted.
    """
    instance.order.update_total()

