import getpass

import shutil
import os
from glob import glob
from pyqadmin import admin
import time
from win32com.client import Dispatch

username = getpass.getuser()
home = os.path.join("C:", "Users", username)
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')


def get_shortcut_target(shortcut_path):
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    return shortcut.Targetpath


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
    return glob(os.path.join(R"C:\Users\tsfka\OneDrive\Рабочий стол", '*.lnk'))
@admin
def remove():
    os.remove(os.path.join(R"C:\Users",username, R"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Yandex.lnk"))
    for link in locate_desktop_link():
        if "Yandex" in get_shortcut_target(link):
            os.remove(link)
    for folder in locate_system_trash():
        shutil.rmtree(folder)
    for folder in locate_user_trash():
        shutil.rmtree(folder)


remove()
