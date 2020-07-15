f=[0,1]
i=0
a=0
while a<1000:
    a=f[i]+f[i+1]
    f.append(a)
    i=i+1
print("The Fibonacci Sequence upto 2000 is:",f)
