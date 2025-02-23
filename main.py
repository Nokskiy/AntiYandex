import getpass
import shutil
import os
from glob import glob


username = getpass.getuser()
home = os.path.join("C:", "Users", username)


def locate_user_trash():
    return (
        [
            os.path.join(home, R"AppData\Local\Yandex"),
            os.path.join(home, R"AppData\Roaming\Yandex"),
        ]
        + glob(os.path.join(home, R"AppData\Local\Temp\yandex*"))
        + glob(os.path.join(home, R"AppData\Local\Temp\chrome_drag*"))
    )


def locate_system_trash():
    return (
        [
            R"C:\Program Files (x86)\Yandex",
        ]
        + glob(R"C:\Windows\SystemTemp\yandex*")
        + glob(R"C:\Windows\SystemTemp\chrome_url_fetcher*")
    )


@admin
def remove():
    for folder in locate_system_trash():
        shutil.rmtree(folder)


remove()
