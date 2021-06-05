# 1 задание
'''
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''
import os

path = []

def print_nested(d, pr=''):
    if isinstance(d, dict):
        for k, v in d.items():
            pr = pr + k + '/'
            print_nested(v, pr)
    elif isinstance(d, list):
        for i, v in enumerate(d):
            pr = pr
            print_nested(v, pr)
    elif isinstance(d, str):
        path.append(pr+d)
    return path

def run_project(d):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(str(project))
    for i in d:
        path = []
        for v in i.split('/'):
            path.append(v)
        path_f = ''
        for ind, n in enumerate(path):
            if len(path) - 1 > ind:
                path_f = path_f + n + '/'
                if not os.path.isdir(path_f):
                    os.mkdir(path_f)
            if len(path) - 1 == ind:
                with open(path_f+path[ind], 'w', encoding='UTF-8') as f:
                    pass
    print(f'Проект [{dir}] распакован в {os.getcwd()}')

rep = False
get_com = ['']
dir = '[проект не открыт]'
indir = []
file = ''

project = {}

while True:
    get_com = list(input(f'Введите команду (? - список команд) {dir} ').split(' '))
    if get_com[0] == '?':
        print('Это программа для создания виртуального дерева файловой системы и ее распаковки')
        print('newproject имя_проекта - создать и открыть новый проект')
        print('openproject имя_файла_проекта.yaml - открыть проект')
        print('showproject - показать всю структуру проекта ')
        print('test - распаковать проект в системе')
        print('exit - выйти из проекта')
        print('show - показать содержимое текущей директории')
        print('open имя_директории - зайти в директорию')
        print('ex - выйти из директории')
        print('addir имя_директории - создает новую директорию')
        print('rmdir имя_директории - удаляет директорию')
        print('redir имя_директории новое_имя_директории - переименовывает директорию')
        print('addfile имя_файла - создает новый файл')
        print('refile имя_файла - переименовывает файл')
        print('rmfile имя_файла - удаляет файл')
    elif get_com[0] == 'newproject':
        if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
            print('Вы не указали имя проекта')
        else:
            import ast
            file = get_com[1]+'.yaml'
            text = "{'"+get_com[1]+"': []}"
            with open(file, 'a', encoding='UTF-8') as f:
                f.write(text)
            with open(file, 'r', encoding='UTF-8') as f:
                project = ast.literal_eval(f.readline())
            for k, v in project.items():
                dir = k
                indir = v
    elif get_com[0] == 'openproject':
        if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
            print('Вы не указали файл проекта')
        else:
            try:
                import ast
                with open(get_com[1], 'r', encoding='UTF-8') as f:
                    project = ast.literal_eval(f.readline())
                file = get_com[1]
                for k, v in project.items():
                    dir = k
                    indir = v
            except FileNotFoundError:
                print(f'Файл проекта [{get_com[1]}] не найден')
            except ValueError:
                print(f'Файл проекта [{get_com[1]}] не содержит проекта или проект поврежден')
    elif get_com[0] == 'exit':
        if file == '':
            exit(1)
        else:
            quest = ''
            while True:
                quest = input('Сохранить проект? (y - да, n - нет, e - отменить выход) ')
                if quest == 'y':
                    with open(file, 'w', encoding='UTF-8') as f:
                        f.write(str(project))
                    exit(1)
                elif quest == 'n':
                    exit(1)
                elif quest == 'e':
                    break
    elif get_com[0] == 'run':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            for k, v in project.items():
                if os.path.isdir(k):
                    print(f'Директория [{k}] существует')
                else:
                    run_project(print_nested(project))
    elif get_com[0] == 'show':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(indir) == 0:
                print('Нет директорий и файлов')
            for i in indir:
                if isinstance(i, dict):
                    for k, v in i.items():
                        print(k, '[dir]')
                else:
                    print(i, '[file]')
    elif get_com[0] == 'showproject':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            path = print_nested(project)
            for i in path:
                print(i)
    elif get_com[0] == 'open':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию')
            else:
                find_dir = False
                for i in indir:
                    if isinstance(i, dict):
                        if get_com[1] in i:
                            find_dir = True
                            dir = f'{dir}/{get_com[1]}'
                            indir = i[get_com[1]]
                if find_dir == False:
                    print(f'Директории [{get_com[1]}] не существует')
    elif get_com[0] == 'ex':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            outdir = dir.split('/')
            outdir.pop()
            if len(outdir) == 0:
                print('Вы находитесь в корневой директории проекта')
            elif len(outdir) > 0:
                for k, v in project.items():
                    dir = k
                    indir = v
                outdir.remove(outdir[0])
                for i, val in enumerate(outdir):
                    for i_v in indir:
                        if isinstance(i_v, dict):
                            if val in i_v:
                                dir = f'{dir}/{val}'
                                indir = i_v[val]
    elif get_com[0] == 'addir':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию')
            else:
                add_dir = True
                for i in indir:
                    if isinstance(i, dict):
                        for k, v in i.items():
                            if k == get_com[1]:
                                print(f'Директория [{get_com[1]}] уже существует')
                                add_dir = False
                if add_dir == True:
                    indir.append({get_com[1]: []})
    elif get_com[0] == 'rmdir':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию')
            else:
                quest = ''
                isdir = False
                for ind, i in enumerate(indir):
                    if isinstance(i, dict):
                        for k, v in i.items():
                            if k == get_com[1]:
                                while True:
                                    quest = input(f'Вы точно хотите удалить директорию [{get_com[1]}]? ')
                                    if quest == 'y':
                                        indir.pop(ind)
                                        isdir = True
                                        break
                                    elif quest == 'n':
                                        isdir = True
                                        break
                if isdir == False:
                    print(f'Директория [{get_com[1]}] не найдена')
    elif get_com[0] == 'redir':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию')
            elif len(get_com) == 2 or (len(get_com) > 2 and get_com[2] == ''):
                print('Вы не указали новое наименование директории')
            else:
                quest = ''
                isdir = False
                dir_del = False
                not_re = False
                for i in indir:
                    if isinstance(i, dict):
                        for k, v in i.items():
                            if k == get_com[2]:
                                print(f'Директория [{get_com[2]}] уже существует')
                                not_re = True
                            elif k == get_com[1]:
                                if not_re == False:
                                    while True:
                                        quest = input(f'Вы точно хотите переименовать директорию [{get_com[1]}]? ')
                                        if quest == 'y':
                                            value = v
                                            key = k
                                            dict_i = i
                                            isdir = True
                                            dir_del = True
                                            break
                                        else:
                                            isdir = True
                                            break
                if dir_del == True and not_re == False:
                    del dict_i[key]
                    dict_i[get_com[2]] = value
                    print(f'Директория [{get_com[1]}] переименована в [{get_com[2]}]')
                if isdir == False and not_re == False:
                    print(f'Директория [{get_com[1]}] не найдена')
    elif get_com[0] == 'addfile':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали имя файла')
            else:
                add_file = True
                for i in indir:
                    if isinstance(i, str):
                        if i == get_com[1]:
                            print(f'Файл [{get_com[1]}] существует')
                            add_file = False
                if add_file == True:
                    indir.append(get_com[1])
    elif get_com[0] == 'refile':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали имя файла')
            elif len(get_com) == 2 or (len(get_com) > 2 and get_com[2] == ''):
                print('Вы не указали новое имя файла')
            else:
                isfile = False
                not_re = False
                quest = ''
                for ind, i in enumerate(indir):
                    if i == get_com[2]:
                        print(f'Файл [{get_com[2]}] существует')
                        not_re = True
                    elif i == get_com[1]:
                        if not_re == False:
                            while True:
                                quest = input(f'Вы точно хотите переименовать файл [{get_com[1]}]? ')
                                if quest == 'y':
                                    index = ind
                                    isfile = True
                                    break
                                elif quest == 'n':
                                    isfile = False
                                    break
                if isfile == True and not_re == False:
                    indir[index] = get_com[2]
                    print(f'Файл [{get_com[1]}] переименован в [{get_com[2]}]')
                if isfile == False and not_re == False:
                    print(f'Файл [{get_com[1]}] не найден')
    elif get_com[0] == 'rmfile':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали имя файла')
            else:
                isfile = False
                quest = ''
                for ind, i in enumerate(indir):
                    if isinstance(i, str):
                        if i == get_com[1]:
                            while True:
                                quest = input(f'Вы точно хотите удалить файл [{get_com[1]}]? ')
                                if quest == 'y':
                                    indir.pop(ind)
                                    isfile = True
                                    break
                                elif quest == 'n':
                                    isfile = True
                                    break
                if isfile == False:
                    print(f'Файл [{get_com[1]}] не найден')
    else:
        print(f'Команды [{get_com[0]}] нет')