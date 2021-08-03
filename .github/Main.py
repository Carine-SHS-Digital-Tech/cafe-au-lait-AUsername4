P = 'E'
while P == 'E':
    neworsum = input("Would you like to place an order (1)? or view the daily summary? (2): ")
    if neworsum == '1':
        print("""Todays coffe choices are:
1: Cappuccino:   $3.00     
2: Espresso:     $2.25
3: Latte:        $2.50
4: Iced Coffee:  $2.50
""")
        dict =  {1: 'Cappuccino', 2: 'Espresso', 3: 'Latte', 4: 'Iced Coffee'}
        order = 'y'
        while order.lower() == 'y':
            order = input("Would you like to order (y) yes or (n) no?: ")
            print("It worked!")
        else:
            print("End")
    elif neworsum == '2':
        print("THIS IS THE DAILY SUMMARY, COME BACK TO THIS LATER YOU NONCE")
    else:
        print("This is not a valid number")


