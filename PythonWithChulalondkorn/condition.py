# # == ! = <> > < >= <=
# score = 55
# if score > 70 :
#     print("Good")
# else:
#     print("try harder")

def greeting(lang):
    if lang == "th":
        print("sawasdee")
    else:
        print("hello")
def greeting2(lang):
    if lang == "th":
        print("sawasdee")
    elif  lang=="jp":
        print("konichiwa")
    else:
        print("hello")
def meet_req(eng,interview):
    if eng<20 and interview>50:
        return True
    else:
        return False
# greeting("aa")
greeting2("jp")