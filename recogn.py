import speech_recognition as sr
# import os
import subprocess as sb

r = sr.Recognizer()
# r.energy_threshold = 1500000
r.dynamic_energy_threshold = True  # type: bool
r.dynamic_energy_adjustment_ratio = 1.1  # type: float


with sr.Microphone() as source:

    while True:

        # r.adjust_for_ambient_noise(source, 2)
        print("Скажите что-нибудь")
        audio = r.listen(source)

        try:
            com = r.recognize_google(audio, language="ru-RU")
            if "узык" in com:
                # sb.Popen("aimp3 /play", shell=True)
                sb.Popen("D:\Soft\AIMP3\AIMP3.exe /play", shell=True)
                # os.popen("D:\Soft\AIMP3\AIMP3.exe /play")
                print(com)
                # break
            elif "топ" in com:
                # os.popen("D:\Soft\AIMP3\AIMP3.exe /pause")
                sb.Popen("D:\Soft\AIMP3\AIMP3.exe /pause", shell=True)
                print(com)
            else:
                print(com)

        except sr.UnknownValueError:
            print("Робот не расслышал фразу")

        except sr.RequestError as e:
            print("Ошибка сервиса; {0}".format(e))
