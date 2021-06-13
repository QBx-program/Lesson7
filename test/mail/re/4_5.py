import os

size =[]
files = {}
n = 1
d = {}

dir = input('Укажить путь к директории ')

if os.path.isdir(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            f = f'{dirpath}\{file}'
            files[os.path.getsize(f)] = f
            size.append(os.path.getsize(f))

    a = len(str(max(files)))
    for i in range(a):
        n *= 10
        d[n] = [0, []]

    for k, v in files.items():
        for i, n in d.items():
            if len(str(k))+1 == len(str(i)):
                exp = v.split('.').pop()
                n[0] += 1
                if exp not in n[1]:
                    n[1].append(exp)

    for k, v in d.items():
        d[k] = tuple(v)

    print(d)
else:
    print('Директория не найдена или ей не является')






