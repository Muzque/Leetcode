n, m, a = map(int, input().split())
L = n // a + 1 if n % a else n // a
W = m // a + 1 if m % a else m // a
print(L*W)
