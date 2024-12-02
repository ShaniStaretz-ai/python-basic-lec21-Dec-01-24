#fibd: receive index of fib series and return the value
def fibonacci(index):
    a=1
    b=1
    if index<2:
        return 1
    l1=[a,b]
    while len(l1)<=index:
        c=a+b
        l1.append(c)
        a=b
        b=c
    else:
        return l1[index]


print(fibonacci(7))

def fibonacci2(index:int)->None:
    count=2
    a=1
    b=1
    c=0
    if index < 2:
        print(1)
    while count<=index:
        c=a+b
        a=b
        b=c
        count+=1
    else:
        return c

print(fibonacci2(7))