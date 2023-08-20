def find_max(numbers):
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value


num_list = input("Enter a list of numbers separated by spaces: ").split()
num_list = [int(num) for num in num_list]

maximum = find_max(num_list)
print(f"The maximum value in the list is: {maximum}")