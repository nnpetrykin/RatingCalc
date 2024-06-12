print('Калькулятор рейтинга успеваемости и посещаемости студентов'
      '\n*************************************************************************************************'
      '\nДля ввода данных заполняйте поля "Имя: " и "Оценки: ", нажимая Enter после каждого ввода данных.'
      '\n'
      '\nДля прекращения ввода данных и получения результатов:'
      '\n1) Оставьте поле "Имя: " пустым (нажать Enter)'
      '\n2) Оставьте поле "Оценки: " пустым (нажать Enter)'
      '\n')
a = input('Введите 1 и Enter для последующего заполнения полей "Имя: " и "Оценки: " ручным способом.'
          '\nВведите 2 и Enter для автоматической загрузки данных из файла "my_file.txt".'
          '\nВаш выбор: ')
print('*************************************************************************************************')

print('\nВыберите категорию обучающихся:'
      '\n1  - СПО ООД 40.02.01 Право и судебное администрирование (очная) 1 семестр (max. 15 и 40)'
      '\n2  - СПО ООД 40.02.01 Право и судебное администрирование (очная) 2 семестра (max. 5 и 15)'
      '\n3  - СПО 40.02.03 Право и судебное администрирование (очная) 1 семестр (max. 14 и 26)'
      '\n4  - СПО 40.02.03 Право и судебное администрирование (очная) 2 семестра (max. 7 и 10)'
      '\n5  - Специалитет 40.05.03 Судебная экспертиза (очная) 1 семестр (max. 14 и 26)'
      '\n6  - Специалитет 40.05.03 Судебная экспертиза (очная) 2 семестра (max. 7 и 10)'
      '\n7  - Специалитет 40.05.04 Судебная и прокурорская деятельность (очная) 1 семестр (max. 14 и 26)'
      '\n8  - Специалитет 40.05.04 Судебная и прокурорская деятельность (очная) 2 семестра (max. 7 и 10)'
      '\n9  - Бакалавриат 40.03.01 Юриспруденция (очная) 1 семестр (max. 14 и 26)'
      '\n10 - Бакалавриат 40.03.01 Юриспруденция (очная) 2 семестра (max. 7 и 10)'
      '\n11 - Магистратура 40.04.01 Юриспруденция (очная) 1 семестр (max. 14 и 26)'
      '\n12 - Магистратура 40.04.01 Юриспруденция (очная) 2 семестра (max. 7 и 13)'
      '\n13 - Магистратура 40.04.01 Юриспруденция (очная с КЗ или промежуточн. зачетом) 1 семестр (max. 14 и 26)'
      '\n14 - Магистратура 40.04.01 Юриспруденция (очная с КЗ или промежуточн. зачетом) 2 семестра (max. 7 и 10)'
      '\n15 - Специалитет 40.05.04 Судебная и прокурорская деятельность (заочная (без контр.р.)) 1 семестр (max. 14 и 26)'
      '\n16 - Специалитет 40.05.04 Судебная и прокурорская деятельность (заочная (без контр.р.)) 2 семестра (max. 7 и 13)'
      '\n17 - Специалитет 40.05.04 Судебная и прокурорская деятельность (заочная (с контр.р.)) 1 семестр (max. 10 и 20)'
      '\n18 - Специалитет 40.05.04 Судебная и прокурорская деятельность (заочная (с контр.р.)) 2 семестра (max. 5 и 10)'
      '\n19 - Бакалавриат 40.03.01 Юриспруденция (оч.-заочн., заочн. (без контр. р.)) 1 семестр (max. 14 и 26)'
      '\n20 - Бакалавриат 40.03.01 Юриспруденция (оч.-заочн., заочн. (без контр. р.)) 2 семестра (max. 7 и 13)'
      '\n21 - Бакалавриат 40.03.01 Юриспруденция (оч.-заочн., заочн. (с контр. р.)) 1 семестр (max. 10 и 20)'
      '\n22 - Бакалавриат 40.03.01 Юриспруденция (оч.-заочн., заочн. (с контр. р.)) 2 семестра (max. 5 и 10)'
      '\n23 - Магистратура 40.04.01 Юриспруденция (заочная (без контр.р.)) 1 семестр (max. 14 и 26)'
      '\n24 - Магистратура 40.04.01 Юриспруденция (заочная (без контр.р.)) 2 семестра (max. 7 и 13)'
      '\n25 - Магистратура 40.04.01 Юриспруденция (заочная (с контр.р.)) 1 семестр (max. 10 и 20)'
      '\n26 - Магистратура 40.04.01 Юриспруденция (заочная (с контр.р.)) 2 семестра (max. 5 и 10)')

print()
action = input(
    'Введите порядковый номер категории обучающихся (1, 2 ... 26) и нажмите Enter: ')

def exit():
    print('*************************************************************************************************')
    a = input(f'Программа завершила работу. Данные сохранены в файл "result_file.txt"')

# ручной ввод
def calc(max_attendance, max_result):
    c = 1
    name = None
    outer_dict = {}
    inner_dict = {}
    print(f'*************************************************************************************************'
          f'\nВаш выбор: посещаемость, max: {max_attendance}; результаты учебных занятий, max: {max_result}.'
          f'\n*************************************************************************************************')
    try:
        quantity = int(input('Введите количество занятий для расчёта посещаемости и нажмите Enter: '))
        print('*************************************************************************************************')
        while name != '':
            name = input('Имя: ')
            evaluations = input('Оценки: ')
            if '2' in evaluations or '3' in evaluations or '4' in evaluations or '5' in evaluations:
                c = 0
                if '2' in evaluations:
                    c += evaluations.count('2')
                if '3' in evaluations:
                    c += evaluations.count('3')
                if '4' in evaluations:
                    c += evaluations.count('4')
                if '5' in evaluations:
                    c += evaluations.count('5')
            evaluations = evaluations.lower()
            inner_dict = {
                'Посещаемость': round(float(
                    ((quantity - evaluations.count('н') - evaluations.count('б') * 0.25)) / quantity * max_attendance)),
                'Успеваемость': round(
                    float((((evaluations.count('2') * 2 + evaluations.count('3') * 3 + evaluations.count(
                        '4') * 4 + evaluations.count('5') * 5) / c) * max_result) / 5))
            }
            outer_dict[name] = inner_dict
        print('*************************************************************************************************')
        print(f'Посещаемость, max: {max_attendance}. Результаты учебных занятий, max: {max_result}')
        print()
        for i, j in outer_dict.items():
            if i != '':
                print(f'{i}: {j}')
            else:
                continue
        print()
        with open('result_file.txt', 'w', encoding='utf-8') as r:
            for i, j in outer_dict.items():
                r.write((f'{i}: {j}') + '\n')
    except Exception as e:
        print(e, 'Перезапустите программу и в поле общее количество занятий введите число и нажмите Enter')


# считывание из файла
def auto_calc(max_attendance, max_result):
    c = 1
    name = None
    outer_dict = {}
    inner_dict = {}
    print(f'*************************************************************************************************'
            f'\nВаш выбор: посещаемость, max: {max_attendance}; результаты учебных занятий, max: {max_result}.'
            f'\n*************************************************************************************************')
    quantity = int(input('Введите количество занятий для расчёта посещаемости и нажмите Enter: '))
    print('*************************************************************************************************')
    a2, a3, a4, a5, n, b = 1000000, 1000000, 1000000, 1000000, 1000000, 1000000
    f = open('../RatingCalculator/my_file.txt', 'r', encoding='utf-8')
    text = f.read()
    my_list = text.split('\n')
    for i in my_list:
        try:
            if ' 2 ' in i:
                a2 = i.index(' 2 ')
            if ' 3 ' in i:
                a3 = i.index(' 3 ')
            if ' 4 ' in i:
                a4 = i.index(' 4 ')
            if ' 5 ' in i:
                a5 = i.index(' 5 ')
            if ' н ' in i.lower():
                n = i.index(' н ')
            if ' б ' in i.lower():
                b = i.index(' б ')
            name = i[:min(a2, a3, a4, a5, n, b)] # имя
            evaluations = i[min(a2, a3, a4, a5, n, b):] # оценки
        except Exception as e:
            print('*****', e, '*****')

        if '2' in evaluations or '3' in evaluations or '4' in evaluations or '5' in evaluations:
            c = 0
            if '2' in evaluations:
                c += evaluations.count('2')
            if '3' in evaluations:
                c += evaluations.count('3')
            if '4' in evaluations:
                c += evaluations.count('4')
            if '5' in evaluations:
                c += evaluations.count('5')
        evaluations = evaluations.lower()
        inner_dict = {
            'Посещаемость': round(float(
                ((quantity - evaluations.count('н') - evaluations.count('б') * 0.25)) / quantity * max_attendance)),
            'Успеваемость': round(
                float((((evaluations.count('2') * 2 + evaluations.count('3') * 3 + evaluations.count(
                    '4') * 4 + evaluations.count('5') * 5) / c) * max_result) / 5)),
        }
        outer_dict[name] = inner_dict
        f.close()
        print('*************************************************************************************************')
        print(f'Посещаемость, max: {max_attendance}. Результаты учебных занятий, max: {max_result}')
        print()
        for i, j in outer_dict.items():
            print(f'{i}: {j}')
        print()
        r = open('result_file.txt', 'w', encoding='utf-8')
        for i, j in outer_dict.items():
            r.write((f'{i}: {j}') + '\n')
        r.close()

if a == '1':
    if action == '4' or action == '6' or action == '8' or action == '10' or action == '14':
        calc(7, 10)
        exit()
    elif action == '1':
        calc(15, 40)
        exit()
    elif action == '2':
        calc(5, 15)
        exit()
    elif (action == '3' or action == '5' or action == '7' or action == '9' or action == '11' or action == '13' or action ==
        '15' or action == '19' or action == '23'):
        calc(14, 26)
        exit()
    elif action == '12' or action == '16' or action == '20' or action == '24':
        calc(7, 13)
        exit()
    elif action == '17' or action == '21' or action == '25':
        calc(10, 20)
        exit()
    elif action == '18' or action == '22' or action == '26':
        calc(5, 10)
        exit()
    else:
        print('*******************************************************************************************')
        print('Нет такого действия. Программа завершена.')

elif a == '2':
    if action == '4' or action == '6' or action == '8' or action == '10' or action == '14':
        auto_calc(7, 10)
        exit()
    elif action == '1':
        auto_calc(15, 40)
        exit()
    elif action == '2':
        auto_calc(5, 15)
        exit()
    elif (action == '3' or action == '5' or action == '7' or action == '9' or action == '11' or action == '13' or action ==
        '15' or action == '19' or action == '23'):
        auto_calc(14, 26)
        exit()
    elif action == '12' or action == '16' or action == '20' or action == '24':
        auto_calc(7, 13)
        exit()
    elif action == '17' or action == '21' or action == '25':
        auto_calc(10, 20)
        exit()
    elif action == '18' or action == '22' or action == '26':
        auto_calc(5, 10)
        exit()
    else:
        print('*******************************************************************************************')
        print('Нет такого действия. Программа завершена.')
else:
    print('*******************************************************************************************')
    print('Нет такого действия. Программа завершена.')

