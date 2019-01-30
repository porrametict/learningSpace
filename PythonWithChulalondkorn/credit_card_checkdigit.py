def remove_nonedigit(s):
    d = []
    for c in s :
        if c.isdigit():
            d.append(int(c))
    return d
def print_digit(v):
    # for i in v:
    #     print("{:>2} |".format(i),end="")
    [ print("{:>2} |".format(i),end="") for i in v]
    print()
if __name__ == '__main__':
    card = "4597 7692 1332 987"
    card = remove_nonedigit(card)
    # print(remove_nonedigit(card))
    print_digit(range(15))
    print_digit(card)
    a = [2,1]*7 +[2]
    print_digit(a)
    print("-"*70)
    y = [m*n for m,n in zip(card,a)]
    y2 = [n if n<10 else n // 10 + n % 10 for n in y ]
    print_digit(y)
    print_digit(y2)
    sumy2 = sum(y2)
    print("sum = {}".format(sumy2))
    r = sumy2 % 10
    check_digit = 0 if r == 0 else 10-r
    print("Check digit = {}".format(check_digit))


