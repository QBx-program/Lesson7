import os
import shutil

path_tmp = []


if not os.path.isdir('my_project'):
    os.mkdir('my_project')
if not os.path.isdir('my_project/templates'):
    os.mkdir('my_project/templates')
b_pass = 'my_project/'
for dirpath, dirnames, filenames in os.walk('my_project'):
    for dirname in dirnames:
        temp = os.path.join(dirpath, dirname)
        if temp.find('templates') > -1:
            path_tmp = temp.split('\\')
            if len(path_tmp) > 2:
                list_dir = os.listdir('/'.join(path_tmp))
                for l in list_dir:
                    if os.path.isdir('/'.join(path_tmp)+'/'+l):
                        pass
                        try:
                            os.mkdir('my_project/templates/'+l)
                        except Exception as e:
                            print(e)
                for l in list_dir:
                    if os.path.isfile('/'.join(path_tmp) + '/' + l):
                        u_path = []
                        check = False
                        for i in path_tmp:
                            if i == 'templates':
                                check = True
                            if check == True:
                                u_path.append(i)
                        try:
                            shutil.copyfile('/'.join(path_tmp)+'/'+l, b_pass+'/'.join(u_path)+'/'+l)
                        except Exception as e:
                            print(e)
