cash=float(input('موحودی: '))
withdraw=float(input('برداشت: '))
if withdraw <= 0 :
    print('خطا')
elif withdraw <= cash :
    cash-=withdraw
    print('برداشت انجام شد')
    print('موجودی جدید', cash)
else:
    print('موجودی کافی نیست')