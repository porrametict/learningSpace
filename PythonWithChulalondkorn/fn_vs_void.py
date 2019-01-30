def celslus_to_fah(celslus):
    return (celslus*9/5)+32


def temperature_table(): #void function
    for c in range(0,101,5):
        f = celslus_to_fah(c)
        print("{}c ={}f".format(c,f))
# f = celslus_to_fah(100)
# print(f)
def manu(): #void function
    print("1.convert c to f")
    print("2.display tamperature table ")
    n = input()
    if n == "1":
        c = float(input("Enter Value"))
        print("{}c={}f".format(c,celslus_to_fah(c)))
    else:
        temperature_table()

# a=temperature_table()
# print(a)
manu()