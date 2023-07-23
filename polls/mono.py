import requests
import os

from django.conf import settings
from .models import Order, OrderItem


def create_order(order_data):
    basketOrder = []
    order_items = []
    amount = 0
    order = Order.objects.create(total_price=amount)
    for order_item in order_data:
        item_sum = order_item["book_id"].price * order_item["quantity"]
        basketOrder.append(
            {
                "name": order_item["book_id"].book,
                "qty": order_item["quantity"],
                "sum": item_sum,
                "unit": "шт.",
            }
        )
        item = OrderItem.objects.create(
            book=order_item["book_id"], order=order, quantity=order_item["quantity"]
        )
        order_items.append(item)
        amount += item_sum
    order.total_price = amount
    order.save()

    body = {
        "amount": amount,
        "merchantPaymInfo": {"reference": str(order.id), "basketOrder": basketOrder},
        "webHookUrl": "https://craftapi-d7d0310369b0.herokuapp.com/callback/",
    }
    r = requests.post(
        "https://api.monobank.ua/api/merchant/invoice/create",
        headers={"X-Token": settings.MONOBANK_API_KEY},
        json=body,
    )
    r.raise_for_status()
    order.invoice_id = r.json()["invoiceId"]
    order.save()
    url = r.json()["pageUrl"]
    return {"url": url, "id": order.id}
