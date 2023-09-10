# Задание 1. Условие:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) 
# и разархивирования с путями (x).
# *Задание 2. *
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h). 
# Проверить, что хеш совпадает с рассчитанным командой crc32.


import subprocess

folderout = "/home/user/out"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step8():
    #test8
    assert checkout(f"cd {folderout}; 7z l {folderout}/arx2.7z", "2 files")


def test_step9():
    #test9
    assert checkout(f"cd {folderout}; 7z x {folderout}/arx2.7z -y", "/home/user/out/arx2.7z")


def test_step10():
    #test10
    assert checkout(f"cd {folderout}; crc32 {folderout}/test1.txt", "cbf53a1c")
    assert checkout(f"cd {folderout}; crc32 {folderout}/test2.txt", "879a731d")

#Запуск в терминале: $ pytest test_dz_2.py -v
