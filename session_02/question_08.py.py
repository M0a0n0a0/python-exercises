clock=int(input('enter clock: '))
if 0<= clock <12 :
    print("Morning")
elif 12<= clock <16 :
    print("Noon")
elif 16<= clock <20 :
    print("Evening")
elif 20<= clock <=23 :
    print("Night")
else:
    print("error")