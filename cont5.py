def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan
for i in range(5):
    print(fibonacci(i))
