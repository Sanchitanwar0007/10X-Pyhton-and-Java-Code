h = int(input())
lst = []
for val in range(0, h):
    lst.append([int(i) for i in input().split(' ')])
result = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
for i in result:
    i.reverse()
print(len(result))
for val in result:
    print(" ".join(str(i) for i in val))