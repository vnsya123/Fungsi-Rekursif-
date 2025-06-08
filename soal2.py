def is_palindrom(kalimat):
    kalimat = kalimat.replace(" ", "").lower() 
    return cek_rekursif(kalimat)

def cek_rekursif(kalimat):
    if len(kalimat) <= 1:
        return True
    if kalimat[0] != kalimat[-1]:
        return False
    return cek_rekursif(kalimat[1:-1])


kalimat = "Kasur ini rusak"
if is_palindrom(kalimat):
    print("Palindrom")
else:
    print("Bukan palindrom")
