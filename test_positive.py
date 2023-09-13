import yaml
from checkers import checkout, getout
import pytest

# folderin = "/home/user/tst"
# folderout = "/home/user/out"
# folderext = "/home/user/folder1"
# folderbad = "/home/user/folder2"

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


class TestPositive:
    def test_step1(self, after_step):
        #test1
        assert checkout(f'cd {data["folderin"]}; 7z a {data["folderout"]}', "Everything is Ok"), "test1 FAIL"


    def test_step2(self, after_step):
        # test2
        assert checkout(f'cd {data["folderout"]}; 7z e {data["folderout"]}/arx2.{data["extension"]} -o{data["folderext"]} -y', "Everything is Ok"), "test2 FAIL"


    def test_step3(self, after_step):
        # test3
        assert checkout(f'{data["folderout"]}; 7z t {data["folderout"]}/arx2.{data["extension"]}', "Everything is Ok"), "test3 FAIL"

    # Задание 2
    # Добавить в проект тесты, проверяющие работу команд d (удаление из архива) и u (обновление архива).
    # Вынести в отдельные переменные пути к папкам с файлами, с архивом и с распакованными файлами.
    # Выполнить тесты с ключом -v.


    def test_step4(self, after_step):
        # test4
        assert checkout(f'cd {data["folderout"]}; 7z d arx2.{data["extension"]}', "Everything is Ok"), "test4 FAIL"


    def test_step5(self, after_step):
        # test4
        assert checkout(f'cd {data["folderin"]}; 7z u {data["folderout"]}/arx2.{data["extension"]}', "Everything is Ok"), "test5 FAIL"

    # Задание 4
    # Доработать позитивные тесты таким образом, чтобы при
    # архивации дополнительно проверялось создание файла
    # архива, а при распаковке проверялось создание файлов.


    def test_step6(self, after_step):
        #test6
        res1 = checkout(f'cd {data["folderin"]}; 7z a {data["folderout"]}/arx2', "Everything is Ok")
        res2 = checkout(f'ls {data["folderout"]}', "arx2.")
        assert res1 and res2, "test6 FAIL"


    def test_step7(self, after_step):
        #test7
        res1 = checkout(f'cd {data["folderout"]}; 7z e aex2.7z -o{data["folderext"]} -y', "Everything is Ok"), "test7 FAIL"
        res2 = checkout(f'ls {data["folderext"]}', "test1.txt")
        res3 = checkout(f'ls {data["folderext"]}', "test2.txt")
        assert res1 and res2 and res3, "test7 FAIL"


    def test_step8(self, after_step):
        #test8
        assert checkout(f'cd {data["folderout"]}; 7z l arx2.{data["extension"]}', " files"), "test8 FAIL"


    def test_step9(self, after_step):
        #test9
        assert checkout(f'cd {data["folderout"]}; 7z x {data["folderout"]}/arx2.{data["extension"]} -y', "/home/user/out/arx2.7z")

    def test_step10(self, after_step):
        #test10
        hash_crc32 = getout(f'cd {data["folderout"]}; crc32 arx2.{data["extension"]}').upper()
        res1 = checkout(f'cd {data["folderout"]}; 7z h arx2.{data["extension"]}', hash_crc32.upper())
        res2 = checkout(f'cd {data["folderout"]}; 7z h arx2.{data["extension"]}', hash_crc32.lower())
        assert res1 or res2, "NO equal hash"
        

if __name__ == "__main__":
    pytest.main(["-v"])
