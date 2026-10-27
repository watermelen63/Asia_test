ans = []

for i in range(501):
    temp = []

    for j in range(1, i):
        temp2 = []

        if i % j == 0:
            temp2.append(i)
            temp2.append(j)
            temp.append(temp2)

    if len(temp) == 1:
        ans.append(i)

print("輸出:", end = ' ')

for i in ans:
    print(i, end = ' ')

print()
print(f"質數個數: {len(ans)}")