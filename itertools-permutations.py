
from itertools import permutations
String, k = input().split()
k = int(k)
String = sorted(String)
for i in (permutations(String,k)):
    print("".join(i))
