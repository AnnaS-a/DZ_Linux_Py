import string
from random import random
import pytest
import yaml
from checkers import checkout
from datetime import datetime


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()      #фикстура сама создает папки(директории)
def make_folders():
    return checkout(f'mkdir -p {data["folderin"]} {data["folderout"]} {data["folderext"]} {data["folderext3"]} {data["folderbad"]}', "")


@pytest.fixture()      #фикстура сама удаляет папки(директории)
def clear_folders():
    return checkout(f'rm -rf {data["folderin"]}/* {data["folderout"]}/* {data["folderext"]}/* {data["folderext3"]}/* {data["folderbad"]}/*', "")


@pytest.fixture()      #фикстура сама создает файлы и хранит их в списке (произвольные названия и наполнение)
def make_file():
    list_of_file = []    #сгенерировали имя файла из заглавных букв и цифр, всего 5 символов
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folderin"], filename), ""):
            # если файл сгенерировался удачно, то переходим в нашу директорию создаем файл с этим именем, размер 1Мб
            list_of_file.append(filename)
    return list_of_file


@pytest.fixture()      #фикстура создает каталог и файлы или возвращает созданный каталог и файлов нет, или ничего не создалось
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout(f'cd {data["folderin"]}; mkdir {subfoldername}', ""):
        return None, None
    if not checkout(f'cd {data["folderin"]}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs={data["bs"]} count=1 iflag=fullblock', ""):
        return subfoldername, None
    return subfoldername, testfilename


@pytest.fixture()      #фикстура создает каталог fh[bd ytufnbdys[ ntcnjd
def create_bad_archive():
    checkout(f' cd {data["folderin"]}; 7z a {data["folderout"]}/arx2', "Everything is Ok")
    checkout(f' cp {data["folderout"]}/arx2.{data["extension"]} {data["folderbad"]}', '')
    checkout(f'truncate -s 1 {data["folderbad"]}/arx2.{data["extension"]}', '')


@pytest.fixture(autouse=True)      #фикстура создает
def speed():
    print(datetime.now().strftime('%H:%M:%S.%f'))
    yield
    print(datetime.now().strftime('%H:%M:%S.%f'))

# Задание 1. Дополнить проект фикстурой, которая после каждого шага теста дописывает
# в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора
# из файла /proc/loadavg (можно писать просто все содержимое этого файла).


@pytest.fixture()
def after_step():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    files_count = data["count"]
    file_size = data["bs"]
    cpu_load_stats = _get_cpu_load_stats()
    stat_file_path = "stat.txt"

    with open(stat_file_path, "a") as file:
        file.write(f"{timestamp}, {files_count}, {file_size}, {cpu_load_stats}\n")


def _get_cpu_load_stats():
        # получения статистики загрузки процессора из файла /proc/loadavg
    with open("/proc/loadavg", "r") as file:
        cpu_load_stats = file.read()
    return cpu_load_stats
