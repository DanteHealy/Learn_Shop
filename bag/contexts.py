from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        sku = product.sku
        quantity = 1
        total += product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'product': product,
            'sku': sku,
            'quantity': quantity,
        })

    if total > settings.DISCOUNT_THRESHOLD:
        discount = round(total * Decimal(settings.DISCOUNT_PERCENTAGE / 100))
    else:
        discount = 0

    discount_delta = settings.DISCOUNT_THRESHOLD - total

    grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount_delta': discount_delta,
        'grand_total': grand_total,
    }

    return context
