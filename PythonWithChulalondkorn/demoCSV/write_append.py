import datetime


def demo_append():
    with open (r"demo.txt","a",encoding="utf8") as f :
        f.write("lily")
demo_append()

def cash_register():
    d = {"m": "mocha", "l": "latte", "e": "espresso", "c": "cappuccino"}
    with open ("trans.txt","a",encoding="utf8") as f:
        while True :
            menu = input("[m]ocha, [l]atte, [e]spresso, [c]appuccino, [q]uit:")
            if menu != "q" :
                dt = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
                f.write("{},{}\n".format(d[menu],dt))
            else:
                 break

cash_register()