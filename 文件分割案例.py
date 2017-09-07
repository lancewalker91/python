def save_file(boy,girl,count):
    file_boy_name = 'boy' + str(count) + '.txt'
    file_girl_name = 'girl' + str(count) + '.txt'

    boy_file = open(file_boy_name, 'w')
    girl_file = open(file_girl_name, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(name):
    f = open(r'C:\Users\PC\Desktop\python\ceshi.txt')
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':',1)
            if role == '李涛':
                boy.append(line_spoken)
            if role == '马静':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    f.close()
split_file(r'C:\Users\PC\Desktop\python\ceshi.txt')


