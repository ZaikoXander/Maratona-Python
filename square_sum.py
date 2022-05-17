def square_sum(numbers):

    final_numbers = []
    
    for i in range(len(numbers)):
        num = numbers[i] ** 2
        final_numbers.append(num)

    final_numbers_sum = sum(final_numbers)

    return final_numbers_sum

print(square_sum([1, 2, 2]))
