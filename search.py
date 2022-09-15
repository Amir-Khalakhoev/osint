import io
def get_lines ():
    import io
    while 1<2:
        inf = input("Введите начальную информацию: ")
        with io.open('base.txt', encoding='utf-8') as file:
            for line in file:
                if inf in line:
                    if (line == ""):
                        print("Информация не найдена!")
                    else:
                        print(line, end='')
print(get_lines())