n = int(input())
ans = ["one", "two", "three", "four"]
if n > len(ans) or n < 1:
    print("error")
else:
    print(ans[n - 1])