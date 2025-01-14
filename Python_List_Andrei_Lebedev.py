while True:
    print("\n--- Меню функций строк ---")
    print("1. Строка байтов (b\"byte\")")
    print("2. Конкатенация строк (S1 + S2)")
    print("3. Повторение строки (S1 * 3)")
    print("4. Обращение по индексу (S[i])")
    print("5. Длина строки (len(S))")
    print("6. Замена шаблона (S.replace())")
    print("7. Разбиение строки (S.split())")
    print("8. Проверка, состоит ли строка из цифр (S.isdigit())")
    print("9. Проверка, состоит ли строка из букв (S.isalpha())")
    print("10. Проверка, состоит ли строка из букв или цифр (S.isalnum())")
    print("0. Выход")

    choice = input("Выберите номер функции (0-10): ")
    
    if choice == "1":
        S = b"byte"
        print("Пример: строка байтов:", S)
        print("Используется для работы с двоичными данными.")
    
    elif choice == "2":
        S1 = "Hello"
        S2 = "World"
        print("Пример: конкатенация строк:", S1 + " " + S2)
        print("Используется для объединения строк в одну.")
    
    elif choice == "3":
        S1 = "Repeat"
        print("Пример (Repeat): повторение строки:", S1 * 3)
        print("Используется для создания строк с повторяющимися элементами.")
    
    elif choice == "4":
        S = "Index"
        print("Пример cлова Index: символ по индексу [2]:", S[2])
        print("Используется для доступа к отдельным символам строки.")
    
    elif choice == "5":
        S = "Length"
        print("Пример слова Lenght: длина строки:", len(S))
        print("Используется для определения количества символов в строке.")
    
    elif choice == "6":
        S = "Hello World"
        print("Пример (Hello World): замена 'World' на 'Python':", S.replace("World", "Python"))
        print("Используется для замены части строки на другую строку.")
    
    elif choice == "7":
        S = "Python,Java,C++"
        print("Пример (Python,Java,C++): разбиение строки по запятой:", S.split(","))
        print("Используется для разделения строки на части по заданному разделителю.")
    
    elif choice == "8":
        S = "12345"
        print("Пример (12345): состоит из цифр?", S.isdigit())
        print("Используется для проверки, содержит ли строка только числа.")
    
    elif choice == "9":
        S = "Python"
        print("Пример (Python): состоит из букв?", S.isalpha())
        print("Используется для проверки, содержит ли строка только буквы.")
    
    elif choice == "10":
        S = "Python3"
        print("Пример: состоит из букв или цифр?", S.isalnum())
        print("Используется для проверки, содержит ли строка только буквы и/или цифры.")
    
    elif choice == "0":
        print("Выход из программы.")
        break
    
    else:
        print("Неверный ввод. Попробуйте снова.")