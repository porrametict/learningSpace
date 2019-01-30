def demo_loop():
    s = {"apple", "banana", "mango", "cherry"}
    a = list(s)
    a.sort()
    for f in a :
        print(f)

def demo_loop2():
    countries = {
        ("th", "Thailand"),
        ("jp", "Japan"),
        ("kr", "Korea")
    }
    # print(countries)
    # for c in countries:
    #     print(c[0])
    # for country_id, country_name in countries:
    #     print(country_name)
    for i, (country_id, country_name) in enumerate(countries):
        print("{}. {} {}".format(i + 1, country_id, country_name))

        if ("jp", "Japan") in countries:
            print("found")
        else:
            print("not found")


# demo_loop2()
# demo_loop()

def immutable_set():
    fs = frozenset(["lily","canation"])
    print(fs)
    print(type(fs))
immutable_set()