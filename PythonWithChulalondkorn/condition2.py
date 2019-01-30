def ticket(age):
    if age <= 5 :
        return  0
    else:
        return 100
def ticket2(age):
    if age <= 5 or age >=60 :
        return  0
    else:
        return 100
def ticket2A(age):
    return 0 if age <= 5 or age >=60 else 100 #ternary


def ticket3(age,is_local):
    if age <= 5 or age >=60 and is_local : # and islocal == True
        return  0
    else:
        return 100


# pr?
# print(ticket2(65))55))
print(ticket3(63,False))