import yaml
from checkers import checkout_negative

with open("config.yaml") as f:
    data = yaml.safe_load(f)


class TestNegative:

    def test_step1(self):
        # test1
        result1 = checkout_negative("cd {}; 7z e bad_arx.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "ERROR")
        assert result1, "Test1 FAIL"


    def test_step2(self):
        # test2
        assert checkout_negative("cd {}; 7z t bad_arx.7z".format(data["folder_out"]), "ERROR"), "Test2 FAIL"
