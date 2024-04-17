num_day = ""

for i in range(32):
    if i == 0:
        print("Пн Вт Ср Чт Пт Сб Вс")
        continue
    i = str(i)
    if len(i) == 1:
        i = f" {i}"
    num_day += i + " "
    if int(i) % 7 == 0 and int(i) < 31:
        print(num_day)
        num_day = ""
print(num_day)
