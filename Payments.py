>>> starter_subscription_price = stripe.Price.create(
...   unit_amount=1200,
...   currency="usd",
...   recurring={"interval": "month"},
...   product=starter_subscription['id'],
... )
>>> 
>>> # Save these identifiers
>>> print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
Success! Here is your starter subscription product id: prod_OMTh8d50XJOypd
>>> print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")
Success! Here is your starter subscription price id: price_1NZkkS2tXu0CfXKwLB5PFZb9
>>> # Set your secret key. Remember to switch to your live secret key in production.
>>> # See your keys here: https://dashboard.stripe.com/apikeys
>>> import stripe
>>> stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"
>>> 
>>> stripe.Price.create(
...   currency="usd",
...   unit_amount=1000,
...   product="{{PRODUCT_ID}}",
... )

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"

stripe.PaymentLink.create(line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}])
