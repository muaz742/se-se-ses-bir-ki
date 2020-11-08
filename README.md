# se-se-ses-bir-ki

Python ile text-to-speech kütüphaneleri kullanım çalışmamda oluşan kayıtların bulunduğu depo.

## Kurulum

Gerekli kütüphaneleri kurmak için [pip](https://pip.pypa.io/en/stable/) paket yöneticisi kullanılmalı.

[metinToSes.py](metinToSes.py) dosyası için;
```bash
pip install gTTS
```

[sesToMetin.py](sesToMetin.py) dosyası için;
```bash
pip install SpeechRecognition
```

komutlarını kullanarak gerekli kütüphaneler kurulabilir.

## Kullanım

### metinToSes.py

Ses dosyasına dönüştürülmek istenen metin terminal üzerinden yazılır.
Oluşturulan ses, aynı klasör içerisine ses dosyası (*.mp3) dosyası olarak kayıt edilir.

### sesToMetin.py

Dönüştürülmek istenen ses dosyası seçilir.
Oluşturulan metin, aynı klasör içerisine metin dosyası (*.txt) olarak kayıt edilir.

## Katkı

Çekme istekleri kabul edilir. Büyük değişiklikler için lütfen önce neyi değiştirmek istediğinizi tartışmak üzere bir konu açın.

## Lisans
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)