def read_demo(filename):
    with open(filename,mode="r") as f :
        s = f.readlines()
    print(s)
    s2 = [line.strip() for line in s ]
    print(s2)
filename = "d:/Pyrthon/PythonWithChulalondkorn/data/planet.txt"
read_demo(filename)

filename2 = "d:/Pyrthon/PythonWithChulalondkorn/data/planet2.txt"

def read_demo4(filename):
    with open(filename, mode="r", encoding="utf8") as f:
        s = f.readlines()
    print(s)
    s2 = [a.strip().split(",") for a in s]
    s3 = [a.split(",") for a in s]
    print(s2)
    print(s3)
read_demo4(filename2)