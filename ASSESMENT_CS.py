count = True
total = []
while count:
    number = int(input("Number?"))
    if number == 0:
        count = False
    else:
        total.append(number)
total_1 = 0
for value in total:
    total_1 += value
print(f"total: {total_1}")
        