def find_non_paired_element(arr):
    result = 0
    for num in arr:
        result ^= num  
    return result


count = int(input("Enter the number of elements in the list: "))

arr = []

i = 0
while i < count:
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
    i += 1

non_paired_element = find_non_paired_element(arr)
print(f"The element without a pair is: {non_paired_element}")
