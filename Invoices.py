# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"

stripe.PaymentLink.create(
  line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}],
  invoice_creation={"enabled": True},
)
# CREATING INVOICES FOR THE CUSTOMER WITH THE API KEY
>>> import stripe
>>> stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"
>>> 
>>> stripe.PaymentLink.create(
...   line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}],
...   invoice_creation={
...     "enabled": True,
...     "invoice_data": {
...       "description": "Invoice for Product X",
...       "metadata": {"order": "order-xyz"},
...       "account_tax_ids": ["DE123456789"],
...       "custom_fields": [{"name": "Purchase Order", "value": "PO-XYZ"}],
...       "rendering_options": {"amount_tax_display": "include_inclusive_tax"},
...       "footer": "B2B Inc.",
...     },
...   },
... )
