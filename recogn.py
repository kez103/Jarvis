import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 500

with sr.Microphone() as source:

    while True:

        print("Скажите что-нибудь")
        audio = r.listen(source)

        try:
            print(r.recognize_google(audio, language="ru-RU"))
        except sr.UnknownValueError:
            print("Робот не расслышал фразу")
            # pass
        except sr.RequestError as e:
            print("Ошибка сервиса; {0}".format(e))
