# def demo():
#     i = 1
#     while i <= 10 :
#         print(i)
#         # i = i+1
#         i +=1
#     print("end loop")
# def demo_for ():
#     for i in range(1,11):
#         print(i)
#
# demo()
# demo_for()
def sum_input():
    n = int(input("enter n "))
    total = 0
    while n != 0: # while....do
        total += n
        n = int(input("enter n "))
    print("total = ",total)


sum_input()

def sum_input_repeat_unit():
    total = 0
    while True: # do ...while
        n = int(input("enter n "))
        if n != 0:
            total+=n
        else:
            break
    print("total=",total)
sum_input_repeat_unit()