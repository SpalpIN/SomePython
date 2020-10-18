import os

def makeDirs():
    path = input("Введите имя каталога: ")

    path_list = path.split(r'\\')

    path = ''
    res=''

    if len(path_list[0]) == 2 and list(path_list[0])[1] == ':':
        try:
            os.mkdir(path_list[0])
        except FileNotFoundError:
            res = 'Не удалось найти том %s' %list(path_list[0])[0]
        except FileExistsError:    
            path += r'{}'.format(path_list[0])
    else: 
        res = 'Введена некоректная строка'

    if path:
        del path_list[0]
        for i in path_list:
            try:
                os.mkdir(path + r'\\'+ i)    
            except FileExistsError:    
                path += r'\\'+ i
                res = "Создать директорию %s не удалось, так как файл с таким именем уже существует" % i
            except OSError:
                res = "Создать директорию %s не удалось" % i
                break
            else:          
                path +=  r'\\'+ i  
                res= "Успешно создана директория %s" % path
    return res

if __name__ == '__main__':
    print(makeDirs())