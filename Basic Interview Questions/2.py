# 2. Check a string is  Palindrome 

# Input: "madam"
# Output: True

# name = input("Enter a string:")
# rev=name[::-1]

# if name == rev:
#     print("True")
# else:
#     print("False") 

#Check a number is palindrome

num=int(input("Enter the number:"))
n=num
reverse=0

while num>0:
    last_digit=num%10
    reverse=reverse*10+last_digit
    remove_last_digit=num//10
print(reverse)    