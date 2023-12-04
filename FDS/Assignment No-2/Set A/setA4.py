def dist(x,y,n):
    sum=0
    for i in range (n):
         for j in range(i+1,n):
             sum+=(abs(x[i]-x[j])+abs(y[i]-y[j]))
    return sum
x=[-1,1,3,2]
y=[5,6,5,3]
n=len(x)
print("Sum of marhattan distance :",dist(x,y,n))
"""
output:-
ty32@pc38:~/TYBCS-32/FDS/Assignment No-2$ python3 setA4.py
Sum of marhattan distance : 22
"""
