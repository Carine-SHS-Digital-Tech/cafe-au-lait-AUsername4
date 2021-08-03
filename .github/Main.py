print("""Todays coffe choices are:
1: Cappuccino:   $3.00     
2: Espresso:     $2.25
3: Latte:        $2.50
4: Iced Coffee:  $2.50
""")
e == int(input("Which coffee would you like to order?"))

cupcount == cupcount +1
if e == 1:
    capnum = capnum +1
    cost = (3*1.1)
    surcharge = (3*0.1)
    totalsur = totalsur + surcharge
    totalcost = totalcosst + cost
elif e == 2:
    espnum = espnum +1
    cost = (2.25*1.1)
    surcharge = (2.25*0.1)
    totalsur = totalsur + surcharge
    totalcost = totalcosst + cost
elif e == 3:
    latnum = latnum +1
    cost = (2.5*1.1)
    surcharge = (2.5*0.1)
    totalsur = totalsur + surcharge
    totalcost = totalcosst + cost
elif e == 4:
    icenum = icenum +1
    cost = (2.5*1.1)
    surcharge = (2.5*0.1)
    totalsur = totalsur + surcharge
    totalcost = totalcosst + cost
else:
    print("Sorry that is not a valid order")
