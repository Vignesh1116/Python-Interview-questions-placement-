# Move Zeros to End

arr = [0, 1, 0, 3, 12]

result = []

zeros = 0

for num in arr:
    if num == 0:
        zeros += 1
    else:
        result.append(num)

for i in range(zeros):
    result.append(0)

print(result)