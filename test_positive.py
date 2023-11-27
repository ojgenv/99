import yaml
from checkers import checkout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


class TestPositive:

    def test_step1(self, make_files):
        # test1
        result1 = checkout("cd {}; 7z a {}/arx2".format(data["folder_in"], data["folder_out"]), "Everything is Ok")
        result2 = checkout("cd {}; ls".format(data["folder_out"]), "arx2.7z")
        assert result1 and result2, "test1 FAIL"

    def test_step2(self, make_files):
        # test2
        result1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(data["folder_out"], data["folder_ext"]),
                            "Everything is Ok")
        result2 = checkout("cd {}; ls".format(data["folder_ext"]), "glit")
        result3 = checkout("cd {}; ls".format(data["folder_ext"]), "king")
        assert result1 and result2 and result3, "test 2 FAIL"

    def test_step3(self):
        # test3
        assert checkout("cd {}; 7z t arx2.7z".format(data["folder_out"]), "Everything is Ok"), "Test3 FAIL"

    def test_step4(self):
        # test4
        assert checkout("cd {}; 7z u {}/arx2.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test4 FAIL"

    def test_step5(self):
        # test5
        assert checkout("cd {}; 7z d arx2.7z".format(data["folder_out"]), "Everything is Ok"), "Test5 FAIL"
