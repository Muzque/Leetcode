n, k = map(int, input().split())
a_list = list(map(int, input().split()))
print(sum(x >= (a_list[k-1] or 1) for x in a_list))
