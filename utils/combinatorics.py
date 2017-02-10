def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def permutation(n, k):
    return int(factorial(n) / factorial (n-k))

def combinations(n, k):
    return int (factorial(n) / (factorial(n-k) * factorial (k)))

if __name__ == "__main__":
    print (factorial(3))
    print (permutation(3, 2))
    print (combinations(3, 2))
