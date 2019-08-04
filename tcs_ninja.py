 # Explanation : absolute difference of sum of even and sum of odd number places. length of input might be maximum 100
''' input_case:1 
    4258
    output_case:1
    1
    input_case:2
    541236
    output_case:2
    3

'''
import math
n=int(input())
a=[]
odd=0
even=0
y=n
for _ in range(100):
    y=y/10
    a.append(y%10)
    if(y==0):
        break
a.reverse()
for i in range(len(a)):
    if(i%2==0):
        odd+=a[i]
    else:
        even+=a[i]
print(abs(odd-even))
    
