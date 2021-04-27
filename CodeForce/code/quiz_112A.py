a = list(ord(x) for x in input().lower())
b = list(ord(x) for x in input().lower())
c = 0
for j in range(len(a)):
    if a[j] > b[j]:
        c = 1
        break
    elif a[j] < b[j]:
        c = -1
        break
print(c)

# print((a>b)-(a<b))

