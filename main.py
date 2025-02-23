import os,psutil,getpass

def get_user():
    return getpass.getuser()

def locate_yandex():
    return "C:/Users/" + get_user() + "/AppData/Local/Yandex/YandexBrowser/Application"
print(locate_yandex())