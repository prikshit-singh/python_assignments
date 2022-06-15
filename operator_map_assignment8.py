import time
import operator

l1 = [1,2,3]
l2 = [2,3,4]

t1 = time.time()
a,b,c = map(operator.mul,l1,l2)

print(t1)
print(a,b,c)