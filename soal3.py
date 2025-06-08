def faktorial(n):
    if n <= 1:
        return 1
    return n * faktorial(n - 1)

def jumlah_ganjil(n):
    if n <= 0:
        return 0
    if n % 2 == 1:  # ganjil
        return n + jumlah_ganjil(n - 2)
    else:  # genap
        return jumlah_ganjil(n - 1)

def jumlah_ganjil_hingga_faktorial(n):
    return jumlah_ganjil(faktorial(n))

n = 4  # maka 4! = 24
print("Jumlah ganjil dari 1 sampai", faktorial(n), "adalah:", jumlah_ganjil_hingga_faktorial(n))
