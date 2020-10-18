
def takeMsg():
    filename = input('Введите имя файла: ')
    user_mes_type = input('Введите тип сообщений E-ошибки, W-предупреждения, I - информация, A - все сообщения: ')

    if user_mes_type == 'A':
        user_mes_type = ('E', 'W', 'I')

    res_dict = {}
    res_list = []
    file_pos = 0

    with open('{}'.format(filename), 'r') as f:
        for line in f:
            if 'MVF' in line:
                line_list = line.split()
                mes_type = list(line_list[0])[-1]

                if len(line_list[0]) == 9 and mes_type in user_mes_type:  
                    res_dict['msg'] = line_list[0]                    
                    del line_list[:1]   
                    res_dict['type'] = mes_type
                    res_dict['offset'] = file_pos
                    res_dict['text'] = ' '.join([str(elem) for elem in line_list])
                    print(res_dict)
            file_pos += len(line)

if __name__ == '__main__':
    msg_list = takeMsg()
