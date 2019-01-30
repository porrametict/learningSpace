def demo():
    print(("{}{}".format("th","thailand")))
    print(("{:5}|{:15}|".format("th", "thailand")))   #align left
    print(("{:>5}|{:>15}|".format("th", "thailand"))) #align right
    print(("{:*>5}|{:->15}|".format("th", "thailand")))  # align right
    print(("{:^5}|{:^15}|".format("th", "thailand"))) #align center

def mult_table(n):
    for i in range(1,13):
        print("{} x {:2} = {:3}".format(n,i,n*i))

def demo_dict():
    menu = {"name":"mocha","price":40, "size":"m"}
    print(menu["name"])
    print('menu name = {} price = {}'.format(menu["name"],menu["price"]))
    print('menu name = {name} ({size}) price = {price}'.format(**menu))
# demo()
# demo_dict()
mult_table(12)