import string
import random
import pytest
import yaml
from checkers import ssh_checkout
from files import upload_files

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(autouse=True, scope="module")
def make_folders():
    return ssh_checkout("0.0.0.0", "user2", "1111",
                        "mkdir -p {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                      data["folder_ext2"]),
                        "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout("0.0.0.0", "user2", "1111",
                        "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"],
                                                                                               filename, data["bs"]),
                        ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture(autouse=True, scope="module")
def clear_folders():
    return ssh_checkout("0.0.0.0", "user2", "1111",
                        "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                            data["folder_ext2"]), "")


@pytest.fixture(autouse=True, scope="module")
def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "1111", "/home/user/p7zip-full.deb", "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "1111", "echo '1111' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "1111", "echo '1111' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)
