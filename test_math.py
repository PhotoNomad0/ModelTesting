# write a Python program to print out the first 100 prime numbers
def generate_primes():
    primes = []
    for num in range(2, 100):
        is_prime = True
        for i in range(2, num):
            if (num % i == 0):
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(generate_primes())