# Задание
# Напишите программу по следующему условию:
# Все четные числа в диапазоне от 0 до 10 суммируются в переменной A. Все числа в диапазоне от 10 до 20, которые делятся на 3, умножаются в переменной B, а те, которые делятся на 2 и 3 суммируются в значение C.

A = 0 # Сумма начинается с 0
B = 1 # Произведение с 1
C = 0 # Сумма с 0

for i in range(0, 20):
	if i < 10:
		if i % 2 == 0:
			A = A + i
	else:
		if i % 3 == 0:
			if i % 2 == 0:
				C = C + 1
			else:
				B = B * i