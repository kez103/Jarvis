import speech_recognition as sr
# import os
import subprocess as sb

r = sr.Recognizer()
r.dynamic_energy_threshold = False  # type: bool
# r.energy_threshold = 1500
# r.dynamic_energy_adjustment_ratio = 1.1  # type: float


with sr.Microphone() as source:

    # r.energy_threshold = 1500

    while True:

        try:

            r.adjust_for_ambient_noise(source)
            # r.energy_threshold = 500
            print("Скажите что-нибудь")
            audio = r.listen(source=source, timeout=3, phrase_time_limit=3)
            # r.energy_threshold = 1500
            print(r.energy_threshold)  # type: float
            # audio = r.listen(source=source)

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

        except sr.WaitTimeoutError:
            pass
