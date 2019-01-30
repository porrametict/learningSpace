def demo_reader():
    f = open("flower.txt")
    data = f.read()
    print(data)
    f.close()
# demo_reader()

def demo_readline():
    f = open("flower.txt")
    data = f.readline()
    print(data)
    data2 = f.readline()
    print(data2)
    f.close()
# demo_readline()

def demo_readlines():
    f = open("flower.txt")
    data = f.readlines() # return list
    print(data)
    # data2 = f.readline()
    # print(data2)
    f.close()
# demo_readlines()

def demo_readline2():
    f = open("flower.txt")
    for i in range(3):
        print(f.readline(),end ="")
    f.close()
# demo_readline2()

def demo_readlines2():
    f = open("flower.txt")
    for line  in f :
        print(line.capitalize(),end="")
    f.close()
demo_readlines2()