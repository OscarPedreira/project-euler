import math

# a + b + c = 1000
# a^2 + b^2 = c^2
# a < b < c
# a + b + sqrt(a^2 + b^2) = 1000

for a in range(1, 1000):
    for b in range(1, 1000):
        if a < b:
            if a + b + math.sqrt(a**2 + b**2) == 1000:
                a = int(a)
                b = int(b)
                c = int(math.sqrt(a**2 + b**2))
                print(a, b, c)
                print(a * b * c)
