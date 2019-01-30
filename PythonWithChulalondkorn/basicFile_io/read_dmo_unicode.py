def demo_reader():
    with open("flower.txt") as f :
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)
# demo_reader()
def demo_reader2():
    with open("d:/Pyrthon/PythonWithChulalondkorn/data/flower.txt") as f :
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)
# demo_reader2()
def demo_reader_unicode():
    with open("d:/Pyrthon/PythonWithChulalondkorn/data/province.txt",mode="r",encoding="utf8" ) as f :
        print(f.name)
        print(f.mode)
        # i = 1
        # for line in f :
        #     print("{}.{}".format(i,line),end="")
        #     i = i + 1
        for i,line in enumerate(f):
            print("{}.{}".format(i+1, line), end="")
demo_reader_unicode()