def findMean(a, n1):
    sum = 0
    for i in range( 0, n1):
        sum += a[i]
     
    return float(sum/n1)
def findMedian(a, n1):
    sorted(a)
    if n1 % 2 != 0:
        return float(a[n1/2])
     
    return float((a[int((n1-1)/2)] +
                  a[int(n1/2)])/2.0)
a = [ 2,3,1 ]
n1 = len(a)
print("Median =", findMedian(a, n1))
