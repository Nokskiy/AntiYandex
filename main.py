import getpass,shutil,os
from pyqadmin import admin

def get_user():
    return getpass.getuser()
def get_disk_plus_user():
    return "C:/Users/" + get_user()
def locate_trash():
    yandex = get_disk_plus_user() + "/AppData/Local/Yandex/YandexBrowser/Application"
    yandex_roaming = get_disk_plus_user() + "/AppData/Roaming/Yandex"
    yandex_local = get_disk_plus_user() + "/AppData/Local/Yandex"
    yandex_programm_files = "C:/Program Files (x86)/Yandex"
    trash = [yandex,yandex_roaming,yandex_local,yandex_programm_files]
    return trash
@admin
def remove():
    shutil.rmtree(r"C:/Program Files (x86)/Yandex")
remove()