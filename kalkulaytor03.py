while True:
    a= input('первое число')
    if a == "exit":
        break
    a=int(a)
    v= input('возвести в квадрат? (1-да, 2-нет)')
    if v == "exit":
        break
    v=int(v)
    if v == 1:
        x=a*a
    elif v == 2:
        b= input('второе число')
        if b == "exit":
            break
        b=int(b)
        c= input('1-плюс, 2-минус, 3-умножить, 4-разделить')
        if c == "exit":
            break
        match c:
            case "1":
                x= a+b 
            case "2":
                x= a-b
            case "3":
                x= a*b
            case "4":
                x=a/b
    print(x)

