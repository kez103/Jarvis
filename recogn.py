import speech_recognition as sr
from commands import exeCom

r = sr.Recognizer()
r.dynamic_energy_threshold = False  # type: bool
# r.energy_threshold = 1500
# r.dynamic_energy_adjustment_ratio = 1.1  # type: float


with sr.Microphone() as source:

    # r.energy_threshold = 1500

    while True:

        try:

            r.adjust_for_ambient_noise(source)
            # print(r.energy_threshold)  # type: float
            # r.energy_threshold = 500
            # print("Скажите что-нибудь")

            audio = r.listen(source=source, timeout=1, phrase_time_limit=2)
            # r.energy_threshold = 1500

            # audio = r.listen(source=source)

            com = r.recognize_google(audio, language="ru-RU")

            if "жар" in com:

                print("Сэр")
                print(com)
                audio = r.listen(source=source, timeout=1, phrase_time_limit=2)
                com = r.recognize_google(audio, language="ru-RU")

                if not exeCom(com):
                    print("Сэр, команда не найдена")

        except sr.UnknownValueError:
            print("Робот не расслышал фразу")

        except sr.RequestError as e:
            print("Ошибка сервиса; {0}".format(e))

        except sr.WaitTimeoutError:
            pass
