record=0
for i in range (1,11):
    height= float (input('enter jump height: '))
    if height>record :
        record=height
        print('بیشترین پرش ثبت شده')
    elif height==record :
        print ('مناسب')
    elif height<0 :
        print('نامعتبر')
    else:
        print('تغییر نکرده')
        