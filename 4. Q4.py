def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    squared = str(n ** 2)
    return squared.endswith(str(n))

num = int(input("Enter a number: "))

print(f"{num} is Prime: {is_prime(num)}")
print(f"{num} is Perfect: {is_perfect(num)}")
print(f"{num} is Armstrong: {is_armstrong(num)}")
print(f"{num} is Palindrome: {is_palindrome(num)}")
print(f"{num} is Automorphic: {is_automorphic(num)}")
