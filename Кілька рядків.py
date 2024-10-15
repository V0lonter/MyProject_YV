def has_same_characters(word):
    return len(set(word)) == 1

N = int(input("Кількість слів: "))

count = 0

for i in range(N):
    word = input(f"Введіть слово {i + 1}: ")
    if has_same_characters(word):
        count += 1

print(f"\nКількість слів, що складаються з однакових символів: {count}")