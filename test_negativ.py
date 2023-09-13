import yaml
import pytest
from checkers import checkout_negative


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


# Задание 3
# Создать отдельный файл для негативных тестов. Функцию
# проверки вынести в отдельную библиотеку. Повредить архив
# (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами
# распаковки (e) и проверки (t) поврежденного архива.


class TestNegative:
    def test_step1(self, make_folders, create_bad_archive, after_step):
        # test2
        assert checkout_negative(f'cd {data["folderbad"]}; 7z e {data["folderbad"]}/arx2.{data["extension"]} -o{data["folderext"]} -y', "ERRORS"), "test1 FAIL"

    def test_step2(self, make_folders, create_bad_archive, after_step):
        # test2
        assert checkout_negative(f'cd {data["folderbad"]}; 7z t arx2.{data["extension"]}', "Is not"), "test2 FAIL"


if __name__ == "__main__":
    pytest.main(["-v"])
