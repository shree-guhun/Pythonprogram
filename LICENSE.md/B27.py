str1=int(input())
try:
    i = float(str1)
except (ValueError, TypeError):
    print('\nNo')
print('Yes')
