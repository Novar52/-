while True:
    x= None
    a= int(input('первое число'))
    v= int(input('возвести в квадрат? (1-да, 2-нет)'))
    if v == 1:
        x=a*a
    elif v == 2:
        b= int(input('второе число'))
        c= input('1-плюс, 2-минус, 3-умножить, 4-разделить')
        match c:
            case "1":
                x= a+b 
            case "2":
                x= a-b
            case "3":
                x= a*b
            case "4":
                if b == 0:
                    print('на ноль делить нельзя')
                    continue
                x=a/b
    print(x)
    if input('Выйти из программы?(Yes)') == 'Yes':
        break
