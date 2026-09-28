from math import sin 
s = 0
for n in range(1, 21):
    s += (0.5 ** (2 * n)) / (n**2 + n) * sin(n)
print(s)