N = int(input("Введите количество чисел N:"))
sum = 0 
for i in range(N):
    num = int(input("Введите число:"))
    if num >0:
        sum += num 
print(f"Сумма положительных чисел: {sum}")
