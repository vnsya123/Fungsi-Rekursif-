def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + jumlah_digit(n // 10)
angka = 234
print("Jumlah digit dari", angka, "adalah:", jumlah_digit(angka))
