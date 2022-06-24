print ('для закрытия программы нажмите ctrl+c')
while True:
    a= input('первое число')
    a=int(a)
    v= input('возвести в квадрат? (1-да, 2-нет)')
    v=int(v)
    if v == 1:
        r=a*a
        print (r)
    elif v == 2:
        b= input('второе число')
        b=int(b)
        c= input('1-плюс, 2-минус, 3-умножить, 4-разделить')
        match c:
            case "1":
                x= a+b
                print (x)   
            case "2":
                x= a-b
                print (x)
            case "3":
                x= a*b
                print (x)
            case "4":
                x=a/b
                print (x)
