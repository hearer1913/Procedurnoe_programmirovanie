numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
miss_number = 4
sum_of_numbers = sum(numbers[:miss_number]) + sum(numbers[miss_number+1:])
average_of_numbers = sum_of_numbers/(len(numbers))
numbers[miss_number] = average_of_numbers
print("Измененный список:", numbers)
