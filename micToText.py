import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    print('Dinleniyor...')
    audio_data = r.record(source, duration=5)
    print("Dönüştürülüyor...")
    # convert speech to text
    text = r.recognize_google(audio_data, language='tr-TR')
    print(text)