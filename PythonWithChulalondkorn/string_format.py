def demo():
    frist_name = "peter"
    last_name = "parker"
    age = 21
    print(frist_name,last_name,age)
    print("fristname: {} lastname: {} age:{}".format(frist_name,last_name,age))
    print("lastname: {1} firstname: {0} age:{2}".format(frist_name,last_name,age)) #position


def demo_number():
    n = 2181231521
    print("{}".format(n))
    print("{:,}".format(n))

    d= 15643215.122132
    a = -1324.50
    b = -232.25
    # print("{}".format(d))
    # print("{:.2f}".format(d))
    print("{:,.2f}".format(d))
    print("{:,.2f}".format(a))
    print("{:,.2f}".format(b))

    print("-"*50)
    print("{:20,.2f}".format(d)) #align right
    print("{:=20,.2f}".format(a))
    print("{:20,.2f}".format(b))

demo_number()