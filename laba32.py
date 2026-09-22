import math
a = 0.1
b = 0.9
step = 0.05
n = int(round((b-a)/step)) + 1
print(f"{'x':>7} | {'y':>10}")
print("-" * 20)
for i in range(n):
    x = a + i * step
    part1 = 5 ** math.asin(x/2)
    part2 = math.log(x * math.sin(x), 5)
    y = part1 - part2
    print(f"{x:7.2f} | {y:10.5f}")