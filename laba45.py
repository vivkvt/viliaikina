pr = 1
for n in range(1, 21):
    v = 2**(n/2) + n **3.2 + 1 
    n = n**3 + 2 * (n **2) + 3 
    pr = pr * (v/n)
print(pr)
