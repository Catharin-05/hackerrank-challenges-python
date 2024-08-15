# input N and M (odd numbers)
N, M = map(int, input().split())
n = N//2

# above the WELCOME text
for i in range(n):
    print((".|."*((2*i)+1)).center(M,"-"))
  
# WELCOME text
print("WELCOME".center(M,"-"))

# below the WELCOME text
for i in range(n-1,-1,-1):
    print((".|."*((2*i)+1)).center(M,"-"))
        
