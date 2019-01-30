def ractangle(w,h): #diamamic typing
    # code block
    area = w * h
    return  area
def triangle(w,h):
    # area = .5 *w*h
    return  .5 *w*h
#main entry point
print("1.ragtangle")
print('2.triangle')

n = input("plase select")
w = int(input("width = "))
h = int(input("height = "))

if (n=="1"):
    print("ractangle")
    print(ractangle(w,h))
else:
    print("triangle")
    print(triangle(w,h))