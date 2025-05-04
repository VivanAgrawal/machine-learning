a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a>b and a<c or a<b and a>b:
    print(a,"is middle number")
elif b>a and b<c or b<a and b>c:
    print(b,"is middle number")
elif c>a and c<b or c<a and c>b:
    print(c, "is middle number")
elif a==b==c:
    print("all numbers are equal")
else:
    print("no middle number")
    