import getpass

# import shutil
import os
from glob import glob

username = getpass.getuser()
home = os.path.join("C:", "Users", username)
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')


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


def locate_desktop_link():
    return [
        str(
            glob(os.path.join(r"C:\Users\tsfka\OneDrive\Рабочий стол", '*.lnk'))
        )
    ]


def remove():
    print(desktop)
    for link in locate_desktop_link():
        print(link)
    # for folder in locate_system_trash():
    #    shutil.rmtree(folder)
    # for folder in locate_user_trash():
    #    shutil.rmtree(folder)


remove()
