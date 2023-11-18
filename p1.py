
#a="jjkd"
#b="fuhfg"

try:
    o = input("Enter_The_arithmatic_operater = ")
    b =eval(input("a: "))
    a = eval(input("b: "))
    if(o=='+'):
            print(f"Addition:{a+b}")
    elif(o=='-'):
            print(f"Subtraction:{a-b}")
    elif(o=='*'):
            print(f"Multiplecation:{a*b}")
    elif(o=='/'):
            print(f"Devide:{a/b}")
    elif(o=='%'):
            print(f"Module:{a%b}")
    elif(o=='//'):
            print(f"Intdevide:{a//b}")
    elif(o=='**'):
            print(f"pow:{a**b}")
    else:
            print("Invalid")
except Exception as e:
    print("Variable x is not defined", e)
     



