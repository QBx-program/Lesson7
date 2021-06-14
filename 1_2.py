import os

path = []

def save_project(file, project, files):
    while True:
        quest = input('Сохранить проект? (y - да, n - нет) ')
        if quest == 'y':
            with open(file, 'w', encoding='UTF-8') as f:
                f.writelines(f'{str(project)}\n')
                f.writelines(f'{str(files)}\n')
            break
        elif quest == 'n':
            break

def del_file(path):
    delete = False
    for ind, value in enumerate(files):
        if value[1].find(path) > -1:
            i = ind
            delete = True
            break
    if delete == True:
        files.pop(i)
        delete = False

def open_file(path_file):
    byte_check = False
    try:
        with open(path_file, 'r', encoding='UTF-8') as f:
            in_file = f.read()
        return [in_file, byte_check]
    except UnicodeDecodeError:
        byte_check = True
        with open(path_file, 'rb') as f:
            in_file = f.read()
        return [in_file, byte_check]
    except FileNotFoundError:
        print(f'Файл [{path_file}] не найден\n')
        return ''

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

def run_project(d, proj, fil):
    save_project(prof, fil)
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
    print(f'Проект [{project_name}] распакован в {os.getcwd()}\n')

rep = False
get_com = ['']
dir = '[проект не открыт]'
indir = []
files = []
file = ''

project = {}

while True:
    get_com = list(input(f'\nВведите команду (? - список команд) {dir} ').split(' '))
    if get_com[0] == '?':
        print('Это программа для создания виртуального дерева файловой системы и ее распаковки. Работа с файлами *.irp\n')
        print('newproject имя_проекта - создать и открыть новый проект (расширение указывать не надо)')
        print('openproject имя_файла_проекта - открыть проект (расширение указывать не надо)')
        print('save - сохраняет проект')
        print('saveproject имя_файла - сохрать проект в файл (расширение указывать не надо)')
        print('showproject - показать всю структуру проекта\n')
        print('run - распаковать проект в системе')
        print('exit - выйти из проекта\n')
        print('show - показать содержимое текущей директории')
        print('open имя_директории - зайти в директорию')
        print('ex - выйти из директории\n')
        print('addir имя_директории - создает новую директорию')
        print('rmdir имя_директории - удаляет директорию')
        print('redir имя_директории новое_имя_директории - переименовывает директорию\n')
        print('addfile имя_файла - создает новый пустой файл')
        print('addfile имя_файла путь_к_файлу - копирует файл из ОС в проект')
        print('refile имя_файла - переименовывает файл')
        print('rmfile имя_файла - удаляет файл')
    elif get_com[0] == 'newproject':
        if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
            print('Вы не указали имя проекта\n')
        else:
            import ast
            file = get_com[1]+'.irp'
            text = "{'"+get_com[1]+"': []}\n[]"
            with open(file, 'a', encoding='UTF-8') as f:
                f.write(text)
            with open(file, 'r', encoding='UTF-8') as f:
                project = ast.literal_eval(f.readline())
            for k, v in project.items():
                dir = k
                indir = v
    elif get_com[0] == 'openproject':
        if len(get_com) == 1 or (len(get_com) > 1 and f'{get_com[1]}.irp' == ''):
            print('Вы не указали файл проекта\n')
        else:
            try:
                import ast
                file = f'{get_com[1]}.irp'
                with open(file, 'r', encoding='UTF-8') as f:
                    project = ast.literal_eval(f.readline())
                    files = ast.literal_eval(f.readline())
                for k, v in project.items():
                    dir = k
                    indir = v
                    project_name = indir
            except FileNotFoundError:
                print(f'Файл проекта [{get_com[1]}] не найден\n')
            except Exception:
                print(f'Файл проекта [{get_com[1]}] не содержит проекта или проект поврежден\n')
    elif get_com[0] == 'exit':
        if file == '':
            exit(1)
        else:
            quest = ''
            while True:
                quest = input('Сохранить проект? (y - да, n - нет, e - отменить выход) ')
                if quest == 'y':
                    with open(file, 'w', encoding='UTF-8') as f:
                        f.writelines(f'{str(project)}\n')
                        f.writelines(f'{str(files)}\n')
                    exit(1)
                elif quest == 'n':
                    exit(1)
                elif quest == 'e':
                    break
    elif get_com[0] == 'run':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            for k, v in project.items():
                if os.path.isdir(k):
                    print(f'Директория [{k}] существует\n')
                else:
                    run_project(print_nested(project), project, files)
                    if len(files) > 0:
                        for value in files:
                            if value[0] == True:
                                with open(value[1], 'wb') as f:
                                    f.write(value[2])
                            else:
                                with open(value[1], 'w', encoding='UTF-8') as f:
                                    f.write(value[2])
                    exit(0)
    elif get_com[0] == 'show':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(indir) == 0:
                print('Нет директорий и файлов\n')
            for i in indir:
                if isinstance(i, dict):
                    for k, v in i.items():
                        print(k, '[dir]')
                else:
                    print(i, '[file]')
    elif get_com[0] == 'showproject':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            path = print_nested(project)
            for i in path:
                print(i)
    elif get_com[0] == 'open':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию\n')
            else:
                find_dir = False
                for i in indir:
                    if isinstance(i, dict):
                        if get_com[1] in i:
                            find_dir = True
                            dir = f'{dir}/{get_com[1]}'
                            indir = i[get_com[1]]
                if find_dir == False:
                    print(f'Директории [{get_com[1]}] не существует\n')
    elif get_com[0] == 'ex':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            outdir = dir.split('/')
            outdir.pop()
            if len(outdir) == 0:
                print('Вы находитесь в корневой директории проекта\n')
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
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию\n')
            else:
                add_dir = True
                for i in indir:
                    if isinstance(i, dict):
                        for k, v in i.items():
                            if k == get_com[1]:
                                print(f'Директория [{get_com[1]}] уже существует\n')
                                add_dir = False
                if add_dir == True:
                    indir.append({get_com[1]: []})
    elif get_com[0] == 'rmdir':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию\n')
            else:
                quest = ''
                isdir = False
                for ind, i in enumerate(indir):
                    if isinstance(i, dict):
                        for k, v in i.items():
                            if k == get_com[1]:
                                while True:
                                    quest = input(f'Вы точно хотите удалить директорию [{get_com[1]}] (y,n)? ')
                                    if quest == 'y':
                                        index_delete = []
                                        print(len(files))
                                        for value in files:
                                            if value[1].find(f'{dir}/{get_com[1]}') > -1:
                                                index_delete.append(value)
                                        for i in index_delete:
                                            files.remove(i)
                                        indir.pop(ind)
                                        isdir = True
                                        break
                                    elif quest == 'n':
                                        isdir = True
                                        break
                if isdir == False:
                    print(f'Директория [{get_com[1]}] не найдена\n')
    elif get_com[0] == 'redir':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали директорию\n')
            elif len(get_com) == 2 or (len(get_com) > 2 and get_com[2] == ''):
                print('Вы не указали новое наименование директории\n')
            else:
                quest = ''
                isdir = False
                dir_del = False
                not_re = False
                for i in indir:
                    if isinstance(i, dict):
                        for k, v in i.items():
                            if k == get_com[2]:
                                print(f'Директория [{get_com[2]}] уже существует\n')
                                not_re = True
                            elif k == get_com[1]:
                                if not_re == False:
                                    while True:
                                        quest = input(f'Вы точно хотите переименовать директорию [{get_com[1]}] (y, n)? ')
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
                    for index, value in enumerate(files):
                        if value[1].find(f'{dir}/{get_com[1]}') > -1:
                            files[index][1] = files[index][1].replace(f'{dir}/{get_com[1]}', f'{dir}/{get_com[2]}')
                    print(f'Директория [{get_com[1]}] переименована в [{get_com[2]}]\n')
                if isdir == False and not_re == False:
                    print(f'Директория [{get_com[1]}] не найдена\n')
    elif get_com[0] == 'addfile':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали имя файла\n')
            elif len(get_com) == 2 or (len(get_com) > 2 and get_com[2] == ''):
                add_file = True
                for i in indir:
                    if isinstance(i, str):
                        if i == get_com[1]:
                            print(f'Файл [{get_com[1]}] существует\n')
                            add_file = False
                if add_file == True:
                    indir.append(get_com[1])
            else:
                in_file = open_file(get_com[2])
                if in_file != '':
                    add_file = True
                    for i in indir:
                        if isinstance(i, str):
                            if i == get_com[1]:
                                print(f'Файл [{get_com[1]}] существует\n')
                                in_file = ''
                                add_file = False
                    if add_file == True:
                        files.append([in_file[1], f'{dir}/{get_com[1]}', in_file[0]])
                        indir.append(get_com[1])
    elif get_com[0] == 'refile':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали имя файла\n')
            elif len(get_com) == 2 or (len(get_com) > 2 and get_com[2] == ''):
                print('Вы не указали новое имя файла\n')
            else:
                isfile = False
                not_re = False
                quest = ''
                for ind, i in enumerate(indir):
                    if i == get_com[2]:
                        print(f'Файл [{get_com[2]}] существует\n')
                        not_re = True
                    elif i == get_com[1]:
                        if not_re == False:
                            while True:
                                quest = input(f'Вы точно хотите переименовать файл [{get_com[1]}] (y,n)? ')
                                if quest == 'y':
                                    index = ind
                                    isfile = True
                                    break
                                elif quest == 'n':
                                    isfile = False
                                    break
                if isfile == True and not_re == False:
                    indir[index] = get_com[2]
                    for index, value in enumerate(files):
                        if value[1].find(f'{dir}/{get_com[1]}') > -1:
                            files[index][1] = files[index][1].replace(f'{dir}/{get_com[1]}', f'{dir}/{get_com[2]}')
                    print(f'Файл [{get_com[1]}] переименован в [{get_com[2]}]\n')
                if isfile == False and not_re == False:
                    print(f'Файл [{get_com[1]}] не найден\n')
    elif get_com[0] == 'rmfile':
        if file == '':
            print('Откройте или создайте проект (воспользуйтесь помощью)\n')
        else:
            if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
                print('Вы не указали имя файла\n')
            else:
                isfile = False
                quest = ''
                for ind, i in enumerate(indir):
                    if isinstance(i, str):
                        if i == get_com[1]:
                            while True:
                                quest = input(f'Вы точно хотите удалить файл [{get_com[1]}] (y,n)? ')
                                if quest == 'y':
                                    indir.pop(ind)
                                    del_file(f'{dir}/{get_com[1]}')
                                    isfile = True
                                    break
                                elif quest == 'n':
                                    isfile = True
                                    break
                if isfile == False:
                    print(f'Файл [{get_com[1]}] не найден\n')
    elif get_com[0] == 'save':
        save_project(file, project, files)
    elif get_com[0] == 'saveproject':
        if len(get_com) == 1 or (len(get_com) > 1 and get_com[1] == ''):
            print('Вы не указали имя файла\n')
        else:
            file = f'{get_com[1]}.irp'
            save_project(file, project, files)
    else:
        print(f'Команды [{get_com[0]}] нет\n')