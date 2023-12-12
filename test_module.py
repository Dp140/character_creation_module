import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['main.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in dir_files, f'Файл `{filename}` не найден в корне репозитория'




#special

#if char_class == 'healer':
        #return (
            #f'{char_name} применил специальное умение'
            #f'«Защита {10 + 30}»'
            #)

#defence

#if char_class == 'healer':
        #return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


#attack

#if char_class == 'healer':
        #return (
            #f'{char_name} нанёс урон противнику'
            #f'равный {5 + randint(-3, -1)}'
            #)