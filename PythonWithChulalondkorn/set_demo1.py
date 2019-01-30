def demo():
    skills = {"Python","C","JAVA"}
    print(skills)
    print(type(skills))
    a = {} # dict
    b = set() # set
    print(type(a))
    print(type(b))
    xy  = {(5,2),(5,5)}
    print(xy)  #
# demo()
def basic_op():
    a = {"mango", "banana", "coconut", "mango", "apple"}
    b = {"cherry", "mango", "apple"}
    m = a | b  # union
    print(m)
    n  = a & b
    print(n)
    p = a - b
    q = a ^ b
    print(p)
    print(q)
basic_op()