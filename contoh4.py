def kali_loop(a,b):
    hasil = 0 
    for i in range(1,b+1):
        hasil = hasil + a
        return hasil 

print(kali_loop(3,4))


def kali_rek(a,b):
    if b == 1:
        return b 
    else:
        return a + kali_rek(a,b-1)
    
print(kali_rek(3,4))