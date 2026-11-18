total = 0

for i in range(1, 101):
    total += i

    if total > 50:
        break

    print(i)

print("Total Sum:", total)