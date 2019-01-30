def basic_method():
    fruits = {"mango", "banana"}
    fruits.add("apple")
    print(fruits)
    fruits.update(("coconut","papaya"))
    print(fruits)
    fruits = fruits | {"cherry", "strawberry", "kiwi", "mango"}
    print(fruits)
    fruits.remove("cherry")
    print(fruits)
    fruits.discard("durian")
    if "durian" in fruits:
        print("55")
    fruits.clear()
    print(fruits)
# basic_method()
def pass_skils(req_skils,applicant_skils):
    return  req_skils <= applicant_skils # req is subset of appicant


def pass_skils2(req_skils,applicant_skils):
    a =  req_skils & applicant_skils
    if len(a) >= 2 :
        return True
    else:
        return False

req = {"Python","R","Java"}
applicant = {"Python", "Julia", "css", "Illustrator"}
print(pass_skils2(req,applicant))