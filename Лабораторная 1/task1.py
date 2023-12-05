numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


sum_of_numbers = sum(numbers[:4]) + sum(numbers[5:])
count_of_numbers = len(numbers)
new_item = sum_of_numbers / count_of_numbers
numbers[4] = new_item

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
