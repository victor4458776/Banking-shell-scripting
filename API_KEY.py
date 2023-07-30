#The idea is to get a customer API-KEY and store it in a banking context with the shell
>>> import stripe
>>> stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
>>> customer = stripe.Customer.retrieve("cu_19YMK02eZvKYlo2CYWjsbgL3",
...                                     api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
... )
