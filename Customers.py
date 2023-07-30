>>> import stripe
>>> stripe.api_key = "test_api_..."

>>> customer = stripe.Customer()
>>> customer = stripe.Customer('JOhn')
>>> print(customer)
{
  "id": "JOhn"
}
#EMAIL ERROR,DATA FAIL
>>> print(customer.data[0].email)
stripe.error.AuthenticationError: Invalid API Key provided: test_api_...
>>> stripe.api_key = "sk_test_..."
>>> customer = stripe.Customer.retrieve("cus_123456789")
>>> customer = stripe.Customer('victoralonsogarcia8@gmail.com')
>>> print(email)
{
  "id": "victoralonsogarcia8@gmail.com"
}
#To generate a valid API key go to POSTMAN or the BANK ACCOUNT FROM THE CLIENT
>>> import stripe
>>> stripe.Customer.list(
...     api_key="postman@user",
...     ing_account="ES18 1234 4567 1892 3412",
...     ing_invoice="2020-01-12"
... )
# RETRIEVE ID from banking customers, go to the bank and copy your credentials (this operation is very unsafe)
>>> stripe.Customer.retrieve("ID")


