# Первая задача на дни недели
print('Введи день')
num = int(input())
if 5 < num < 8:
    print("Это выходной")
elif 0 < num < 6:
    print("Будний день")
else:
    print("Ты ведь в курсе, что в неделе семь дней?") 
#Вторая задача  

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z)

#Третья задача 
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print("Ошибка, вы ввели 0")

#Четвертая  задача 
quarter = int(input())

if quarter == 1:
    print("x > 0, y > 0")
elif quarter == 2:
    print("x < 0, y > 0")
elif quarter == 3:
    print("x < 0, y < 0")
elif quarter == 4:
    print("x > 0, y < 0")
else:
    print("Неверное значение четверти")
#Пятая задача 
x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)}")
