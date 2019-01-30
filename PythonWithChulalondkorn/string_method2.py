#strip / trim
def strio_demoo():
    s = "Thailand"
    t = " Thailand "
    u = t.strip()#del spaecbar before str and After str
    print(s==t)
    print(s==u)

def demo_isdigit(p):
    total = 0
    for c in p :
        #print(c)
        if c.isdigit():
            # print(c)
            total += int(c)
    return total

def removenondigit(s):
    t = ""
    for c in s:
        if c.isdigit():
            t+=c
    return t


# plate = "1mf 4567"
# print(demo_isdigit(plate))

card_id = "(444)-123-15-4564 51"
print(removenondigit(card_id))