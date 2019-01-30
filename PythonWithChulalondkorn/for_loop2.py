# def temperature_table():
#     for celsius in range(101):
#         F = (celsius*9/5)+32
#         print(celsius,"=",F)
# temperature_table()

# def mult_table(from_n,to_n):
#     for i in (from_n,to_n):
#         for j in range(1,13):
#             print("{} x {} = {}".format(i,j,i*j))
#         print("---"*40)
# mult_table(2,5)

for i in range(2,4+1):
    for j in range(1, 13):
        print("{} x {} = {}".format(i, j, i * j))
    print("-" * 40)