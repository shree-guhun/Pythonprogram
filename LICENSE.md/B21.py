def sumofAP( a, d,n1) :
    sum = 0
    i = 0
    while i < n1 :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n1 = 20
a = 2.5
d = 1.5
print (sumofAP(a, d, n1))
