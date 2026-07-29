price=int(input('entrer price tag: '))
if price>1000000 :
    pay=price-(price*15/100)
    print(pay)
elif 500000<price<1000000 :
    pay=price-(price*10/100)
    print(pay)
else : 
    pay=price
    print(pay)