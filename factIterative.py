def fact(num):
    if num < 0:
        return None
    if num == 0:
        return 1
    i=0
    f=1

    while i<num:
        i=i+1
        f=f*i
    return f

print(fact(3))  