from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    """
    Returns a dictionary containing the current state of the shopping bag.

    Parameters:
        request (HttpRequest): The current HTTP request.

    Returns:
        dict: A dictionary containing the bag items, total cost, product count,
              delivery cost, free delivery delta, free delivery threshold, and grand total.
    """

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
