import getpass
import shutil
import os
from glob import glob
from win32com.client import Dispatch


username = getpass.getuser()
home = os.path.join(R"C:\Users", username)
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


def delete(file_path):
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def remove():
    for link in locate_desktop_link():
        if "Yandex" in get_shortcut_target(link):
            delete(link)
            pass
    for folder in locate_system_trash():
        delete(folder)
    for folder in locate_user_trash():
        delete(folder)

remove()