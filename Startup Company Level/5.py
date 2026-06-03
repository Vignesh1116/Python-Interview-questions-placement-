# Balanced Parentheses

s = "{[()]}"

stack = []

d = {
    ')': '(',
    '}': '{',
    ']': '['
}

balanced = True

for ch in s:

    if ch in "({[":
        stack.append(ch)

    else:

        if not stack or stack[-1] != d[ch]:
            balanced = False
            break

        stack.pop()

if balanced and not stack:
    print(True)
else:
    print(False)