# Armstrong Number

n = 153

temp = n
s = 0

while temp:
    digit = temp % 10
    s += digit ** 3
    temp //= 10

if s == n:
    print("Armstrong")