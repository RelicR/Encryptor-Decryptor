import random
abc_en = [chr(ord('a') + i//2) if i % 2 == 0 else chr(ord('A') + i//2) for i in range(52)]
abc_ru = [chr(ord('а') + i//2) if i % 2 == 0 else chr(ord('А') + i//2) for i in range(64)]
abc_dig = [i for i in range(10)]
while 1:
    mode = input("Введите 'enc' для запуска алгоритма шифрования\nВведите 'dec' для запуска алгоритма дешифровки\nВыберите алгоритм работы программы enc/dec\n")
    while mode != "enc" and mode != "dec":
        mode = input("Задан некорректный алгоритм работы программы\nВыберите алгоритм работы программы enc/dec\n")
    text = input("Введите текст (буквы 'Ё' и 'ё' будут заменены на 'Е' и 'е')\n").replace('Ё', 'Е').replace('ё', 'е')
    if mode == "enc":
        enc_text = ''
        key = input("Задайте ключ шифрования\nЕсли ключ шифрования не задан, будет сгенерирован случайный ключ\n")
        if not key:
            key = random.randint(-10000, 10000)
        for i in text:
            if i.isalpha() or i.isdigit():
                if i in abc_en:
                    enc_text += abc_en[((abc_en.index(i)//2 + abc_en.index(i) % 2 + int(key)) * 2 - abc_en.index(i) % 2) % len(abc_en)]
                elif i in abc_ru:
                    enc_text += abc_ru[((abc_ru.index(i)//2 + abc_ru.index(i) % 2 + int(key)) * 2 - abc_ru.index(i) % 2) % len(abc_ru)]
                else:
                    enc_text += str(abc_dig[(abc_dig.index(int(i)) + int(key)) % len(abc_dig)])
            else:
                enc_text += i
        print(enc_text, f"\nkey = {key}")

    else:
        dec_text = ''
        key = input("Задайте ключ шифрования\n")
        for i in text:
            if i.isalpha() or i.isdigit():
                if i in abc_en:
                    dec_text += abc_en[((abc_en.index(i)//2 + abc_en.index(i) % 2 - int(key)) * 2 - abc_en.index(i) % 2) % len(abc_en)]
                elif i in abc_ru:
                    dec_text += abc_ru[((abc_ru.index(i)//2 + abc_ru.index(i) % 2 - int(key)) * 2 - abc_ru.index(i) % 2) % len(abc_ru)]
                else:
                    dec_text += str(abc_dig[(abc_dig.index(int(i)) - int(key)) % len(abc_dig)])
            else:
                dec_text += i
        print(dec_text)
    if input("Желаете продолжить работу с программой?\nВведите 'y', чтобы продолжить; любой другой символ для закрытия программы\n") == "y":
        print("\n"*10)
    else:
        break
