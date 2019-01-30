def avg(*args) :
    print(type(args))
    print(args)
    print(args[0])
    totla = 0
    for i in args:
        totla +=i
    return  totla/len(args)
print(avg(4,7,8,12,9))

print("-"*40)
def print_bullet(*items,bullet="#"):
    for e in items:
        print("{} {}".format(bullet,e))
print_bullet("lily","rose","jasmine","forget me not",bullet="+")