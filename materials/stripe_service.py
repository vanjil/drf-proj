import stripe
from django.conf import settings
from .models import Kurs, Payment 

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def create_product(name, description):
    product = stripe.Product.create(
        name=name,
        description=description
    )
    return product

def create_price(product_id, amount):
    price = stripe.Price.create(
        unit_amount=int(amount * 100),
        currency="usd",
        product=product_id
    )
    return price

def create_checkout_session(price_id, success_url, cancel_url):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': price_id,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session

def create_payment(kurs_id, user_id, amount):
    kurs = Kurs.objects.get(id=kurs_id)
    payment = Payment.objects.create(
        user_id=user_id,
        paid_course=kurs,
        amount=amount,
        payment_method='card'
    )
    return payment
