# Find Largest Element in Array

# Input: [2,7,1,9]
# Output: 9

arr = [2, 7, 1, 9]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)