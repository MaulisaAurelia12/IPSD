## 1. memecahkan masalah unik dengan loop dan if-else
### buat program yang dapat menghasilkan pola berbentuk angka seperti dibawah ini, dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya
'''
1
2 3
5 7 11
13 17 19 23
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_pattern(n):
    primes = []
    num = 1
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def print_pattern(n):
    for i in range(1, n + 1):
        primes = generate_pattern(i)
        row = [str(sum(primes[:j + 1])) for j in range(i)]
        print(' '.join(row))

print_pattern(4)