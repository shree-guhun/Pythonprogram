def findMean(a, n):
    sum1 = 0
    for i in range( 0, n):
        sum1 += a[i]
     
    return float(sum1/n)
def findMedian(a, n):
    sorted(a)
    if n % 2 != 0:
        return float(a[n/2])
     
    return float((a[int((n-1)/2)] +
                  a[int(n/2)])/2.0)
a = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
n = len(a)
print("Median =", findMedian(a, n))
