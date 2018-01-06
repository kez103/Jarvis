from subprocess import Popen


def exeCom(com):

    if "гра" in com:  # Играй
        Popen("D:\Soft\AIMP3\AIMP3.exe /play", shell=True)
        print(com)
        return True

    elif "то" in com:  # Стоп
        Popen("D:\Soft\AIMP3\AIMP3.exe /pause", shell=True)
        print(com)
        return True

    elif "альш" in com:  # Дальше
        Popen("D:\Soft\AIMP3\AIMP3.exe /next", shell=True)
        print(com)
        return True

    elif "аза" in com:  # Назад
        Popen("D:\Soft\AIMP3\AIMP3.exe /prev", shell=True)
        print(com)
        return True

    elif "но" in com:  # Снова
        Popen("D:\Soft\AIMP3\AIMP3.exe /play", shell=True)
        print(com)
        return True

    elif "ромч" in com:  # Громче
        Popen("D:\Soft\AIMP3\AIMP3.exe /volup", shell=True)
        print(com)
        return True

    elif "отка" in com:  # Сотка
        for _ in range(10):
            Popen("D:\Soft\AIMP3\AIMP3.exe /volup", shell=True)
        print(com)
        return True

    elif "иш" in com:  # Тише
        Popen("D:\Soft\AIMP3\AIMP3.exe /voldwn", shell=True)
        print(com)
        return True

    elif "олч" in com:  # Молча
        Popen("D:\Soft\AIMP3\AIMP3.exe /mute", shell=True)
        print(com)
        return True

    else:
        return False


if __name__ == '__main__':
    pass
