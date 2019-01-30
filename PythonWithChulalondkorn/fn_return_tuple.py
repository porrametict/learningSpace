# def price_with_vat(amount):
#     vat = amount*7/107
#     price = amount-vat
#     # t = price,vat #tuple
#     return price,vat
#     # return t
# print(price_with_vat(107))
# a = price_with_vat(200)
# print(a)
# print(type(a))
# print("price =",a[0])
# print("vat=",a[1])
# # p,v = price_with_vat(200)
# print("p=",p,"v=",v)

def thai_are(sqwa):
    rai = sqwa//400
    ngan = (sqwa-(rai*400))//100
    wa = sqwa%100
    return rai,ngan,wa
a = 956
print(thai_are(a))
r,n,v =thai_are(a)
print(r,n,v,sep="-")