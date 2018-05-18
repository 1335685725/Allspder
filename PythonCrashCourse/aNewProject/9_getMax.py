a = input()
b = input()
c = input()
max = a
if a < b:
    max = b
    if b < c:
        max = c
elif a < c:
    max = c
print max