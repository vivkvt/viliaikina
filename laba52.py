N = int(input("Введите количество чисел N:"))
if N <3:
    print("Недостаточно элементов для выполнения условия.")
    exit()
numbers = []
for i in range(N):
    num = float(input(f"Введите число {i+1}:"))
    numbers.append(num)
product = 1
count = 0
for i in range(N):
    if i%3 == 0 and numbers[i] !=0:
        product *= numbers[i]
        count += 1
if count>=3:
    print(f"Произведение ненулевых элементов на позициях, кратных 3: {product}")
else:
    print("Ненулевых элементов на позициях, кратных 3, меньше трех.")