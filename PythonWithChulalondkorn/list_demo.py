def loop_list():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    # for f in inflowers:
    #     print(f)
    #
    # for i in range(len(flowers)):
    #     print("{}.{}".format(i+1,flowers[i]))

    for i,e in enumerate(flowers):
        print("{}.{}".format(i + 1, e))

def loop_list2():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "Japan", "ญี่ปุ่น"),
        ("kr", "Korea", "เกาหลีใต้")
    ]
    for i,cuntry in enumerate(countries):
        print(" {}{}".format(i+1,countries[2]))
loop_list2()