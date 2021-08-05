
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
        cofdict = {1: 3,  2: 2.25, 3: 2.5, 4: 2.5}
        feedict = {1: 0.1, 2: 0.05}
        quantdict = {}
        pricedict = {}
        order = input("Would you like to order (y) yes or (n) no?: ")
        while order.lower() == 'y':
            coffee = input("What coffee would you like to order?: ")
            amount = int(input("How many would you like to order: "))
            if coffee == '1':

                price = cofdict[1]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                quantdict['Cappuccino'] = amount
                pricedict['Cappuccino'] = price
                print(round(sgst, 3))
                print(round(tgst, 3))
                print(quantdict)
                print(pricedict)
            elif coffee == '2':

                price = cofdict[2]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                quantdict['Espresso'] = amount
                pricedict['Espresso'] = price
                print(round(sgst, 3))
                print(round(tgst, 3))
                print(quantdict)
                print(pricedict)
            elif coffee == '3':

                price = cofdict[3]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                quantdict['Latte'] = amount
                pricedict['Latte'] = price
                print(round(sgst, 3))
                print(round(tgst, 3))
                print(quantdict)
                print(pricedict)
            elif coffee == '4':

                price = cofdict[4]*amount
                sgst = feedict[1]*cofdict[1]
                tgst = sgst*amount
                quantdict['Iced Coffee'] = amount
                pricedict['Iced Coffee'] = price
                print(round(sgst, 3))
                print(round(tgst, 3))
                print(quantdict)
                print(pricedict)
            else:
                print("That is not a valid ")
            order = input("Would you like to order (y) yes or (n) no?: ")
            dineortake = input("Would you like to dine in?(1) or take away?(2): ")
            if dineortake = '2':
        else:
            print("End")
    elif neworsum == '2':
            print("Daily Summary")
            quit()
    else:
        print("This is not a valid input")
else:
    quit()

