R = input()
print(f"{int(R)}".ljust(10 - len(R) + 1))
print(f"{int(R) / 2:.2f}".ljust(10 - len(R) + 1))
print(f"{(int(R) / 2) ** 2 * 3.1415:.4f}".ljust(10 - len(R) + 1))