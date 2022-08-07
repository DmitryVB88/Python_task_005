# 1. Напишите программу, удаляющую из текста все слова, содержащие ""обв"".


new_list = []
clear_list = []
final_list = str()
path = r'File.txt'
with open(path,'r',encoding = 'utf-8') as f:
    a = (f.read())
    new_list = a.split(' ')
    print(new_list)

    for item in new_list:
          if 'обв' not in item:
             clear_list.append(item)
    final_list = ' '.join(clear_list)
    print(final_list)
    print(type(final_list)) 
with open(path, 'a', encoding= 'utf-8') as f:    
    f.write(f'{final_list}')

