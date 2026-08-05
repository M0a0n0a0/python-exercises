color1= input('enter color: ')
color2= input('enter color: ')
color3= input('enter color: ') 
if color1 == color2 == color3:
    print('all are same')
elif color1 == color2 or color2 == color3 or color3==color1 :
    print('two of them are same')
else:
    print('non is same')