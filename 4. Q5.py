'''Generate all Pythagorean Triplets with side length <= 30.'''
print("Pythagorean Triplets with side lengths ≤ 30:\n")

for a in range(1, 31):
    for b in range(a, 31):  # Start from a to avoid duplicates like (3,4,5) and (4,3,5)
        for c in range(b, 31):
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")
