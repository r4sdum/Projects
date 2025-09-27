print("Добро пожаловать в игру 'Викторина'!\n\t(prod by r4sdum)")
while True:
    incorrect = 0
    goal = 0
    start = str(input("Введите 'start' чтобы начать: ")).lower()
    if start == "start":
        print("\n1. Какая аббревиатура означает 'Информационные технологии'?")
        print(f"\n\tA) IT\n\tB) AI\n\tC) IoT\n\tD) UX\n")
        first_answer = str(input("Введите букву: ")).lower()
        if first_answer == "a":
            goal += 1
        else:
            incorrect += 1
        print("\n2. Какой язык программирования часто называют 'языком веба'?")
        print(f"\n\tA) Python\n\tB) Java\n\tC) JavaScript\n\tD) C++\n")
        second_answer = str(input("Ввод: ")).lower()
        if second_answer == "c":
            goal += 1
        else:
            incorrect += 1
        print("\n3. Что означает аббривиатура 'HTTP'?")
        print(f"\n\tA) HyperText Transfer Protocol\n\tB) High-Tech Transfer Program\n\tC) Hyper Transfer Text Protocol\n\tD) Home Tool Transfer Protocol\n")
        third_answer = str(input("Ввод: ")).lower()
        if third_answer == "a":
            goal += 1
        else:
            incorrect += 1
        print("\n4. Как называется атка, при которой злоумышленник подменивает IP-адрес и перехватывает трафик между двумя узлами?")
        print(f"\n\tA) Фишинг\n\tB) DDoS\n\tC) MITM (Man-in-the-Middle)\n\tD) SQL-инъекция\n")
        fourth_answer = str(input("Ввод: "))
        if fourth_answer == "c":
            goal += 1
        else:
            incorrect += 1
        print("\n5. Какой принцип ООП (объектно-ориентированного программирования) позволяет объектам разных классов обрабатывать один и тот же метод по-своему?")
        print(f"\n\tA) Инкапсуляция\n\tB) Наследование\n\tC) Полиморфизм\n\tD) Абстракция\n")
        fifth_answer = str(input("Ввод: ")).lower()
        if fifth_answer == "c":
            goal += 1
        else:
            incorrect += 1
        print("\nПодсчет результатов:")
        if goal == 5:
            print("5/5 - Ты IT-гуру!")
            break
        elif goal == 4:
            print("4/5 - Отлично, почти идеально!")
            next_try = str(input("Попробовать снова Y/N: ")).lower()
            if next_try == "y":
                continue
            elif next_try == "n":
                break
            else:
                break
        elif goal == 3:
            print("3/5 - Не плохо, но есть куда расти.")
            next_try = str(input("Попробовать снова Y/N: ")).lower()
            if next_try == "y":
                continue
            elif next_try == "n":
                break
            else:
                break
        else:
            print(f"{goal}/5 - Время перечитать пару статей или пройти курс!")
            next_try = str(input("Попробовать снова Y/N: ")).lower()
            if next_try == "y":
                continue
            elif next_try == "n":
                break
            else:
                break
    elif start == "stop":
        print("До встречи!")
        break
    else:
        print("Повторите ввод!\n")
        continue
