#1
text = input("Введіть текст: ")
vowels = "аеєиіїоуюяaeiou"
vowels_count = 0
digit_count = 0
space_count = 0
for char in text.lower():
   if char in vowels:
       vowels_count += 1
   if char.isdigit():
       digit_count += 1
   if char == " ":
      space_count += 1

words_count = len(text.split())
total_chars = len(text)

print(vowels_count)
print(digit_count)
print(space_count)
print(words_count)
print(total_chars)
#2
full_name = input("Введіть ПІБ: ")
parts = full_name.split()

if len(parts) == 3:
    last_name = parts[0].capitalize()
    first_name = parts[1].capitalize()
    patronymic = parts[2].capitalize()
    result = last_name + " " + first_name[0] + "." + patronymic[0] + "."
    print("Одобрено", result)
else:
    print("Перепишіть нормально")

#3
text1 = input("Введіть перший рядок: ")
text2 = input("Введіть другий рядок: ")

text01 = text1.lower().replace(" ", "")
text02 = text2.lower().replace(" ", "")

is_anagram = sorted(text01) == sorted(text02)

print("Нормалізований перший рядок:", text01)
print("Нормалізований другий рядок:", text02)

if is_anagram:
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")

#4
sentence = input("Речення: ")
words = sentence.split()
longest = words[0]
shortest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Найкоротше слово:", shortest)
print("Найдовше слово:", longest)

unique_words = []
for word in words:
    lower_word = word.lower()
    if lower_word not in unique_words:
        unique_words.append(lower_word)
        print("Унакальні:", unique_words)
    else:
        print("Змамініть речення")
