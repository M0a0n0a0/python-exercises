text=input('enter text: ')
if len(text) % 2 ==0 :
    print(text[:len(text)//2])
else:
    print(text[len(text)//2:])