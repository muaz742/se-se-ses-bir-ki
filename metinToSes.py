'''
İşlev: Yazılan metni Türkçe dilinde ses dosyasına dönüştürür.
Girdi: Metin (terminal üzerinden)
Çıktı: Ses dosyası (.mp3)
İşlem adımları;
1. Başla
2. Kullanıcıdan metni al
3. Metni sese dönüştür
4. Hata var mı?
4.0.1. Ses dosyasını kaydet
4.0.2. İşlem sonucunu kullanıcıya bildir
4.1.1. Oluşturulan dosyayı sil
4.1.2. Hata mesajı görüntüle
4.1.3. (opsiyonel) Hata detayı yazdır
5. Dur

Kullandığım kaynaklar
https://pypi.org/project/gTTS/
'''

from gtts import gTTS
import time
import os

# Kullanıcıdan metni al
metin = str(input("Lütfen sese dönüştürmek istediğiniz metni giriniz.\n"))
# metin = 'Al şu takatukaları takatukacıya götür. Eğer takatukacı, takatukaları takatukalamazsa, takatukaları takatukalatmadan geri getir.'

# Metni sese dönüştür
tts = gTTS(metin, lang="tr-TR")
fileName = str(int(time.time()))+".mp3"

# Hata var mı?
try:
    # Ses dosyasını kaydet
    tts.save(fileName)

    # İşlem sonucunu kullanıcıya bildir
    print("Metin ses dosyasına dönüştürüldü. Dosya adı "+ fileName)
except ValueError:
    # Oluşturulan dosyayı sil
    if os.path.exists(fileName):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")
    
    # Hata mesajı görüntüle
    print("Bir hata oluştu\n")

    # Hata detayı yazdır
    # print(ValueError) # hatayı yazdırmak için bu satır aktifleştirilmeli.