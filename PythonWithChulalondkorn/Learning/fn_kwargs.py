def f(**kwargs):#key word args
    print(kwargs)
    print(type(kwargs))
    print(kwargs["age"])
f(name ="Peter",age = 24,hero = "spiderman")

def full_name (**part):
    d = []
    for k in ("fristname","middlename","lastname"):
        if  k in part :
           # print(part[k])
            d.append(part[k])
    return " ".join(d)


    return None
print("-"*50)
s= full_name( fristname="Peter",lastname = "Parker")
print(s)
print("-"*50)
t= full_name(fristname="George",middlename="P",lastname = "Wood")
print(t)
