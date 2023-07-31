#The idea is to get a customer API-KEY and store it in a banking context with the shell
>>> import stripe
>>> stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
>>> customer = stripe.Customer.retrieve("cu_19YMK02eZvKYlo2CYWjsbgL3",
...                                     api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
... )

>>> import stripe
>>> stripe.api_key = "sk_test_CGGvfNiIPwLXiDwaOfZ3oX6Y"
>>> 
>>> starter_subscription = stripe.Product.create(
...   name="Starter Subscription",
...   description="$12/Month subscription",
... )
>>> 
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
