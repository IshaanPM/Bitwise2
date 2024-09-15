def find_two_odd_occurring_numbers(arr):

    xor_all = 0
    for num in arr:
        xor_all ^= num

    set_bit = xor_all & -xor_all  

    num1, num2 = 0, 0
    for num in arr:
        if num & set_bit:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2

arr = list(map(int, input("Enter numbers separated by spaces (make sure exactly two numbers have odd occurrences): ").split()))

odd_occurring_numbers = find_two_odd_occurring_numbers(arr)
print(f"The two numbers that occur an odd number of times are: {odd_occurring_numbers[0]} and {odd_occurring_numbers[1]}")
