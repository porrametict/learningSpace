x = "Joe Doe" # global scope
nums = [5,6,7,8]
print(x)
def fn():
    x = "cat" # local
    print(nums)
    print("inside fn ",x)

def fn2():
    x = "Mr. "+x
    print("inside fn ",x)

def fn3():
    global x
    x = "Mr. "+x
    print("inside fn ",x)
print(x)
fn()
fn3()
print(x)