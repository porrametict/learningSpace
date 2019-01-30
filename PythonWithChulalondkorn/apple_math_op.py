# print(2016%4)
# print(2559%4)
def leap_year(year):
    if year % 4 ==0 :
        return  True
    else:
        return  False
def leap_year_buddhist(year):
    if year % 4 == 3:
        return True
    else:
        return False
def is_even(n):
    return True if n%2==0 else False
    # if n % 2 ==0:
    #     return True
    # else:
    #     return False
def is_odd(n):
    return  not(is_even(n))

def promotion(come,pay,perhead,pax):
    #come 4 pay 2 if come 5 pay ?
    return (pax//come)*(pay*perhead)+(pax%come)*perhead
# print(leap_year(2016))
# print(leap_year_bud dhist(2559))
# print(is_even(5))
# print(is_odd(5))
print(promotion(4,2,100,5))