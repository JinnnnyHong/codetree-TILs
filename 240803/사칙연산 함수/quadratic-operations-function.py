def four(a, o, c):
    operator = ['+', '-', '/', '*']
    if o in operator:
        if o == '+':
            result = a+c
            print(f"{a} + {c} = {result}")
        elif o == "-":
            result = a-c
            print(f"{a} - {c} = {result}")
        elif o == '/':
            result = a//c
            result = int(result)
            print(f"{a} / {c} = {result}")
        else:
            result = a*c
            print(f"{a} * {c} = {result}")
    else:
        print("False")

s,v,t = input().split()

s = int(s)
t = int(t)
four(s,v,t)