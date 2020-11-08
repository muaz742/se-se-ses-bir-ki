''' 
İşlev: Ses dosyasından metin dosyasına dönüştürme.
Girdi: Ses dosyası (.wav .aiff .aif .aifc .flac)
Çıktı: Metin dosyası (.txt)
İşlem adımları;
1. Başla
2. Ses Dosyası seç
3. Seçilen sesi metne dönüştür
4. Metni dosyaya kaydet
5. Oluşturulan dosya içeriğini dosyayı terminalde göster
6. Dur

Kullandığım kaynaklar
https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
https://medium.com/bili%C5%9Fim-hareketi/python-ile-ses-tan%C4%B1ma-uygulamas%C4%B1-olu%C5%9Fturma-3d0d972c62a6
'''

import time
import speech_recognition as sr
import codecs
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Ses dosyası seç
root = tk.Tk()
root.withdraw()

# dosya yolu oluştur
file_path = filedialog.askopenfilename(filetypes=[("Ses dosyaları",".wav .aiff .aif .aifc .flac")])

# Seçilen sesi metne dönüştür
r = sr.Recognizer()
file = sr.AudioFile(file_path)
with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language='tr-TR')

# Metni dosyaya kaydet
pathName = Path(file_path)
pathName = pathName.name
fileName = str(int(time.time()))+"-"+pathName+".txt"
f = codecs.open(fileName, "a", "utf-8")
f.write(result)
f.close()

# Oluşturulan dosya içeriğini dosyayı terminalde göster
f = open(fileName, "r", encoding='utf-8')
print(f.read())