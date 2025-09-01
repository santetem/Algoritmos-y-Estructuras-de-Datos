a,b= 0,1
c = 0
print(a,b)
for i in range(10):
    c= a + b
    a= b
    b=c
    print(a,b,c)