|=== |    |==| ===== |   | |=== |====   |===| /  |   | |====
|    |    |  |   |   |===| |--- |===|   |===/    |   | |===|
|=== |=== |==|   |   |   | |=== ====|   |   \    |===| ====|

Welcome To Clothes R' Us
We keep track of stores, the clothes they stock, and the customers in our system with their own closets to keep track of their past purchases.
We value your patronage and use of our application and wish to work to make your life easy!
Basic Controls:
    When making a selection you will be asked to confirm
        -To confirm please use 'Yes', 'No', 'y', 'n'. (Not case sensitive!)
    To back out to the previous selection list from the Stores List, Your Closet, and any Store Interior
        -Use any of the keywords 'Back', 'Return' (Not case sensitive!)


1. Users may select a customer, or add a new Customer to begin. 
    -New customers need a name and a starting budget of your funds for your shopping adventure.
    -Returning customers need only select their account through their user id. 

2. Next, now that you are logged in, you may:
    Select a store to browse and possibly purchase clothes for yourself. 
            --Note! If your budget is too low for your purchase it will be denied.
                You may always back out of a store to add funds if you wish.
        -From a store you may select an item by its ID for purchase.

    Select 'Add Funds' to add funds to your account.
            --Note! Please use the number you wish to add, not the amount you wish to have total.
                The program will handle the addition of funds for you, valued customer.
    
    Select 'My Closet' to view your purchased clothes.
            --Note! You may remove clothes from your closet, but your money will not be refunded unfortunately due to 
                company policy. We apologize for any inconvenience!


Any and all reviews of us, complaints, and suggestions 
may be sent to clothesrus@nonexistantemail.com 
or tweeted to us @ClothesRUsCorporate

How to create your database:
~ pipenv install 
~ pipenv shell 
~ alembic upgrade head 
~ alembic upgrade --autogenerate -m "commit you change in this message."
    


