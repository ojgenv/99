import string
import random
import pytest
import yaml
from checkers import checkout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(autouse=True, scope="module")
def make_folders():
    return checkout(
        "mkdir -p {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"], data["folder_ext2"]),
        "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename,
                                                                                           data["bs"]), ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture(autouse=True, scope="module")
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_in"], data["folder_ext"], data["folder_ext2"]), "")
