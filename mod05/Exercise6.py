import random
N = int(input("Enter a large number of points: "))
attempt = N
n = 0
while attempt > 0:
    x, y = random.uniform(-1,1), random.uniform(-1,1)
    if x**2 + y**2 < 1:
        n += 1
    attempt -= 1
    
pi = (4 * n) / N
print(f"Approximation of pi: {pi:.4f}")