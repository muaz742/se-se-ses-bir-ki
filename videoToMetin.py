'''
İşlev: bash üzerinde komut ile dönüştürme
Girdi: Video dosyası (filename değişkeni)
Çıktı: Ses dosyası (.wav) (çıktı dosyanın adı actual_filename)
'''
import time
zamanBaslangic = time.time()
import speech_recognition as sr
import codecs
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import os

# Video dosyası seç
root = tk.Tk()
root.withdraw()

# seçilen dosyanın yolunu belirle
v_file_path = filedialog.askopenfilename(
    filetypes=[("Video dosyaları","*.*")]
    )

# dosyanın ismini belirle
soundPathName = Path(v_file_path)
soundPathName = soundPathName.name
soundPathName = str(int(zamanBaslangic))+"-"+soundPathName

print("Videodan ses dosyası ayıklanıyor...")
# video dosyasını ses dosyasına dönüştür
os.system('ffmpeg -i {} -vn {}.wav'.format(v_file_path, soundPathName))
print("Ayıklama işlemi tamamlandı!")
# ses dosyasının dosya yolunu belirle
soundPathName = soundPathName+".wav"

print("Ses dosyası yazıya dönüştürülüyor...")
# Seçilen sesi metne dönüştür
r = sr.Recognizer()
file = sr.AudioFile(soundPathName)
with file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language='tr-TR')
print("Yazıya dönüştürme tamamlandı!")

# Metni dosyaya kaydet
print("Metin dosyası oluşturuluyor...")
pathName = Path(v_file_path)
pathName = pathName.name
fileName = str(int(zamanBaslangic))+"-"+pathName+".txt"
f = codecs.open(fileName, "a", "utf-8")
f.write(result)
f.close()
print("Metin dosyası oluşturuldu: "+fileName)

'''
# Oluşturulan dosya içeriğini dosyayı terminalde göster
f = open(fileName, "r", encoding='utf-8')
print("\nSonuc Yazısı:\n")
print(f.read())
'''

zamanBitis = time.time()
surec = zamanBitis-zamanBaslangic
print("Dönüştürme tamamlandı!\nİşlem {} saniye sürdü.".format(str(int(surec))))