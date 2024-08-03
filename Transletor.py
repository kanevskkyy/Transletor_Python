from sys import exit
easy_level={
    "Cat": "кіт",   "Dog": "собака",   "Sun": "сонце",  "Star": "зірка", "Tree": "дерево"
}

medium_level={
    "Mountain": "гора", "Garden": "сад", "Dinner": "вечеря", "Teacher": "вчитель", "Library": "бібліотека"
}

hard_level={
    "Ubiquitous": "всюдисущий", "Serendipity": "щаслива випадковість", "Ephemeral": "швидкоплинний", "Obfuscate": "затемнювати, заплутувати", "Ineffable": "невимовний"
}

levels={
    0:"Нульовий", 1:"Так собі", 2:"Можна краще", 3:"Норм", 4:"Добре", 5:"Супер"
}

choice_of_level=input("Виберіть режим складності\nЛегкий, Середній, Важкий : ")

words=None

if choice_of_level.lower() == "легкий":
    words=easy_level
elif choice_of_level.lower() == "середній":
    words=medium_level
elif choice_of_level.lower() == "важкий":
    words=hard_level
else :
    print("Упс ... Ви не хочете грати, дуже шкода :(")
    exit()

results={}

for english, ukraine in words.items():
    print(f"{english}, {len(ukraine)} букв, починається на {ukraine[0]} ...")
    answer_of_user=input("Ваш варіант = ")

    if answer_of_user.lower() == ukraine:
        results[english] = True
        english[0].upper()
        print(f"Правильно! {english} - це {ukraine}")

    else:
        results[english] = False
        english[0].upper()
        print(f"Неправильно! {english} - це {ukraine}")

print("Слова, на які дано правильну відповідь : ")

mark = 0

for word in results:
    if results[word]==True:
        mark += 1
        print(word)

if mark != 5:
    print("Слова, на які дано неправильно відповідь : ")
    for word in results:
        if results[word]==False:
            print(word)

print(f"Ваший ранг : {levels[mark]}")