import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd: object, text: object) -> object:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False
