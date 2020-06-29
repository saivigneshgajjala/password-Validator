password = input('''enter password with following conditions:
                    1.minimum of 8 characters
                    2.atleast one lower case
                    3.atleast one upper case
                    4.atleast one number
                    5.atleast one ! or @
enter password : ''')
low=0
num=0
up=0
sp=0
i=0
p = int(len(password))
if p < 8:
    print("enter password with minimum 8 letters")
else:
    for i in range(p):
        if password[i].islower():
            low = low + 1
        elif password[i].isnumeric():
            num = num + 1
        elif password[i].isupper():
            up = up + 1
        elif password[i] == '!' or password[i] == '@':
            sp = sp + 1
    if low > 0 and num > 0 and up > 0 and sp > 0:
        print("password validated")
    else:
        print("enter password with given conditions")
