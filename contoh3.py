import sys
def coba(i):
    if i == 1 :
       return 1
    else :
        return i+coba(i-1)
print(coba(10))


def coba2(n):
    jml = 0
    for i in range(1,n+1):
        jml += i 
    return jml
print(coba2(10))