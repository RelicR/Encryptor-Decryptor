import random
while 1:
    lang = input("Задайте язык текста\nen/ru\n")
    while (lang != "en") * (lang != "ru") == 1:
        lang = input("Введено неверное значение\nЗадайте язык текста\nen/ru\n")
    mode = input("Выберите алгоритм работы программы\nВведите `enc` для запуска алгоритма шифрования\nВведите `dec` для запуска алгоритма дешифровки\n")
    while (mode != "enc") * (mode != "dec") == 1:
        mode = input("Введено неверное значение\nВыберите алгоритм работы программы\nenc/dec\n")
    if mode == "enc":
        enc_text = ""
        if lang == "en":
            key = random.randint(-25, 25)
            text = list(map(str, input("Введите текст на английском языке:\n")))
            temp_text = [chr(abs(ord(i) - 65 + key) % 26 + 65) if not i.islower() and i.isalpha() else i for i in text]
            temp2_text = [chr(abs(ord(i) - 97 + key) % 26 + 97) if i.islower() and i.isalpha() else i for i in temp_text]
            for i in range(len(text)):
                enc_text += temp2_text[i]
            print(enc_text, "\nkey = ", key)
        else:
            key = random.randint(-32, 32)
            text = input("Введите текст на русском языке (не используйте буквы Ё/ё):\n")
            temp_text = [chr((ord(i) - 1040 + key) % 32 + 1040) if not i.islower() and i.isalpha() else i for i in text]
            temp2_text = [chr((ord(i) - 1072 + key) % 32 + 1072) if i.islower() and i.isalpha() else i for i in temp_text]
            for i in range(len(text)):
                enc_text += temp2_text[i]
            print(enc_text, "\nkey =", key)
    else:
        dec_text = ""
        if lang == "en":
            key = int(input("Введите ключ дешифровки\n"))
            text = list(map(str, input("Введите текст на английском языке:\n")))
            temp_text = [chr((ord(i) - 65 + (26 - key) % 26) % 26 + 65) if not i.islower() and i.isalpha() else i for i in text]
            temp2_text = [chr((ord(i) - 97 + (26 - key) % 26) % 26 + 97) if i.islower() and i.isalpha() else i for i in temp_text]
            for i in range(len(text)):
                dec_text += temp2_text[i]
            print(dec_text)
        else:
            key = int(input("Введите ключ дешифровки\n"))
            text = input("Введите текст на русском языке:\n")
            temp_text = [chr((ord(i) - 1040 - key) % 32 + 1040) if not i.islower() and i.isalpha() else i for i in text]
            temp2_text = [chr((ord(i) - 1072 - key) % 32 + 1072) if i.islower() and i.isalpha() else i for i in temp_text]
            for i in range(len(text)):
                dec_text += temp2_text[i]
            print(dec_text)
    if input("\nЖелаете продолжить работу с программой?\nВведите 'y', чтобы продолжить. Введите любой другой символ для закрытия программы\n") == "y":
        print("\n"*10)
    else:
        break