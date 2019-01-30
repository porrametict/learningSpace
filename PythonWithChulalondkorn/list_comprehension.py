def v1():
    for i in range(1, 11):
        print(i, i * 0.621371192)
def kl_to_ml (k):
    return k * 0.621371192
def v2 ():
    # [print(i, i * 0.621371192) for i in range(1, 11)]
    # m = [i * 0.621371192 for i in range(1, 11)]
    n= [kl_to_ml(i) for i in range(1, 11)]
    print(*n)

v2()
def v3():
    m = list(map((lambda i : i * 0.621371192),range(1,11)))
    print(m)
# v3()

