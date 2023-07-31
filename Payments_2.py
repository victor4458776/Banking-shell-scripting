>>> # Set your secret key. Remember to switch to your live secret key in production.
>>> # See your keys here: https://dashboard.stripe.com/apikeys
>>> import stripe
>>> stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"
>>> 
>>> stripe.PaymentLink.create(
...   line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}],
...   after_completion={"type": "redirect", "redirect": {"url": "https://example.com"}},
... )
# After creating a payment link, you can’t delete it. Instead, you can deactivate a payment link by setting 
# the active parameter to false.
# After you deactivate a payment link, customers can no longer complete purchases using the link and are redirected to an expiration
# page instead.
# To reuse a deactivated payment link, reactivate it by setting the active parameter to true.
>>> # Set your secret key. Remember to switch to your live secret key in production.
>>> # See your keys here: https://dashboard.stripe.com/apikeys
>>> import stripe
>>> stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"
>>> 
>>> stripe.PaymentLink.create(
...   line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}],
...   automatic_tax={"enabled": True},
... # Set your secret key. Remember to switch to your live secret key in production.
>>> stripe.PaymentLink.create(
...   line_items=[{"price": "{{10000}}", "quantity": 1}],
...   payment_method_types=["card", "klarna"],
... )
# stripe.error.InvalidRequestError: Request req_WGpRoY7N2YU8gD: No such price: '{{10000}}'

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y'

session = stripe.PaymentLink.create(
  payment_method_types=['card'],
  line_items=[{
    'price': '{{PRICE_ID}}',
    'quantity': 1,
  }],
  consent_collection={
    'terms_of_service': 'required',
  },
)

