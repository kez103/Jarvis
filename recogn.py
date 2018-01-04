import speech_recognition as sr
# import os
import subprocess as sb


def changePlaybak(com):

    if "гра" in com:  # Играй
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /play", shell=True)
        print(com)

    elif "то" in com:  # Стоп
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /pause", shell=True)
        print(com)

    elif "альш" in com:  # Дальше
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /next", shell=True)
        print(com)

    elif "аза" in com:  # Назад
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /prev", shell=True)
        print(com)

    elif "но" in com:  # Снова
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /stop", shell=True)
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /play", shell=True)
        print(com)


def changeVolume(com):

    if "ромч" in com:  # Громче
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /volup", shell=True)
        print(com)

    elif "отка" in com:  # Сотка
        for _ in range(10):
            sb.Popen("D:\Soft\AIMP3\AIMP3.exe /volup", shell=True)
        print(com)

    elif "иш" in com:  # Тише
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /voldwn", shell=True)
        print(com)

    elif "олч" in com:  # Молча
        sb.Popen("D:\Soft\AIMP3\AIMP3.exe /mute", shell=True)
        print(com)


r = sr.Recognizer()
r.dynamic_energy_threshold = False  # type: bool
# r.energy_threshold = 1500
# r.dynamic_energy_adjustment_ratio = 1.1  # type: float


with sr.Microphone() as source:

    # r.energy_threshold = 1500

    while True:

        try:

            r.adjust_for_ambient_noise(source)
            print(r.energy_threshold)  # type: float
            # r.energy_threshold = 500
            print("Скажите что-нибудь")

            audio = r.listen(source=source, timeout=3, phrase_time_limit=3)
            # r.energy_threshold = 1500

            # audio = r.listen(source=source)

            com = r.recognize_google(audio, language="ru-RU")

            changePlaybak(com)
            changeVolume(com)

        except sr.UnknownValueError:
            print("Робот не расслышал фразу")

        except sr.RequestError as e:
            print("Ошибка сервиса; {0}".format(e))

        except sr.WaitTimeoutError:
            pass
