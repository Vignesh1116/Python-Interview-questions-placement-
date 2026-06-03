# Valid Parentheses

s = "()[]{}"

stack = []

d = {
    ')': '(',
    '}': '{',
    ']': '['
}

valid = True

for ch in s:

    if ch in "({[":
        stack.append(ch)

    else:
        if not stack or stack[-1] != d[ch]:
            valid = False
            break

        stack.pop()

if valid and not stack:
    print(True)
else:
    print(False)