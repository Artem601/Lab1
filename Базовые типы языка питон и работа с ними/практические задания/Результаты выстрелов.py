results = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]

# TODO Вычислите необходимые значения
total=sum(results)
count=len(results)
average=total/count


print("Среднее арифметическое результатов выстрелов:", average)
print("Наименьшее количество очков за выстрел:", min(results))
print("Наибольшее количество очков за выстрел:", max(results))
