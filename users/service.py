import stripe
from config.settings import STRIPE_TEST_SECRET_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_TEST_SECRET_KEY

def convert_rub_to_dollars(amount):
    """конвертирует рубли в доллары"""
    c = CurrencyRates
    rate = c.get_rate('RUB', 'USD')
    return int(rate * amount)


def create_stripe_prise(amount):
    """создает цену в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Donatation"},
    )

def create_stripe_session(price):
    """создает ссессию на оплату"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/ ",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")