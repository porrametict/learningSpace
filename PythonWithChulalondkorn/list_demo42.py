
def demo():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    is_exist  = "daisy" in flowers
    print(is_exist)

    # print(flowers.index("calla"))
    # print(flowers.index("daisy"))

    flowers[2] = "Jasmine"
    print(flowers)
    for i in range(len(flowers)):
        flowers[i] = flowers[i].capitalize()
    print(flowers)
    flowers.clear()
    print(flowers)

# demo()

def demo_append():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "Japan", "ญี่ปุ่น"),
        ("kr", "Korea", "เกาหลีใต้")
    ]
    print(countries)
    fr = ("fr","France","ฝรั่งเศษ")
    countries.append(fr)
    print(countries)
    us = ("us","USA","อเมริกา")
    countries.insert(2,us)
    print(countries)
# demo_append()
alphabet = list("ABC")
print(alphabet)
a = [0] *10
print(a)
b = [1,3]* 5
print(b)
