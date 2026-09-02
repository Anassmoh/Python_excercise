import math
import random

N = float(input("Enter a large number of points: "))
point = N

n = 0
while point != 0:
    x, y = random.uniform(-1,1), random.uniform(-1,1)
    # -1 and 1 should not be included

    if x**2 + y**2 < 1:
        n += 1
    point -= 1

pi = (4 * n) / N

print(f"Approximation of pi: {pi:.4f} ")
