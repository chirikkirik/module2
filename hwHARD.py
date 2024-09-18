import random

stone1 = list(range(3, 21))
first_number = random.choice(stone1)

password = ""

for i in range(1,21):
    for j in range(i, 21):
        pair_sum = i + j
        if first_number % pair_sum == 0 and i != j:
            password += f"{i}{j}"

print(first_number)
print(password)






