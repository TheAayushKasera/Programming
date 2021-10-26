from random import *
from pprint import pprint
lst=[]
lst.append(123)
lst.append("122")
lst.extend("abcd")
lst.extend(map(int,"123"))
print(lst)
lst.append("122")
print(lst)
a=list(choice(lst) for i in range(10))
print(a)
print(lst.index("122"))
ab=list()
abcd=lst.copy()
print(abcd.pop(0))
print(abcd)
print(lst)
a="A b c d"
b=a
b=b.split(' ')
print(b,a)