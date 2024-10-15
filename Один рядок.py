line1 = input("Введіть перший рядок: ")
line2 = input("Введіть другий рядок: ")

words = line1.split() + line2.split()

sorted_words = sorted(words, key=len, reverse=True)

print("\nСлова у порядку зменшення їх довжини:")
for word in sorted_words:
    print(word)
