print('Введите длинную строку:')
long_string = input()
if not long_string:
    print('Вы ввели пустую строку, с ней работать не получится')
    exit()
limit = int(input('Введите ограничение на длину короткой строки: '))
if limit < 1:
    print('Ограничение должно быть не меньше 1')
    exit()
while True:
    print('Введите короткую строку. Введите пустую строку, если хотите закончить ввод.')
    line = input()
    if not line:
        break
    if len(line) > limit:
        print('Строка слишком длинная')
        continue
    if line in long_string:
        print(f'{line} является подстрокой')
    else:
        print(f'{line} не является подстрокой')
