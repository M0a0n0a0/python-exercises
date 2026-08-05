number=0
for i in range(1,11):
    if i % 2 == 0:
        i=i+5
        print(i)
        number=number+i
    elif i % 2 != 0:
        j=i*5
        print(j)
        number=number+j
print(number,':','مجموع')
