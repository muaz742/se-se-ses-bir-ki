# importing libraries 
import time
zamanBaslangic = time.time()
import speech_recognition as sr                 # pip3 install SpeechRecognition pydub
import os 
import codecs
from pydub import AudioSegment
from pydub.silence import split_on_silence
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    print("Ses dosyası parçalara ayrılıyor...")
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    print("Parçalara ayırma tamamlandı!")
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language='en-EN')
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

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
#os.system('ffmpeg -i {} -acodec pcm_s16le -ac 1 -ar 16000 {}.wav'.format(v_file_path, soundPathName))
print("Ayıklama işlemi tamamlandı!")
# ses dosyasının dosya yolunu belirle
soundPathName = soundPathName+".wav"

print("Ses dosyası yazıya dönüştürülüyor...")
result = get_large_audio_transcription(soundPathName)
print("\nFull text:\n"+result)
print("Yazıya dönüştürme tamamlandı!")

print("Metin dosyası oluşturuluyor...")
pathName = Path(v_file_path)
pathName = pathName.name
fileName = str(int(zamanBaslangic))+"-"+pathName+".txt"
f = codecs.open(fileName, "a", "utf-8")
f.write(result)
f.close()
print("Metin dosyası oluşturuldu: "+fileName)

print("Geçici veriler siliniyor...")
os.system('rmdir /s /q audio-chunks')
os.system('del /f '+soundPathName)
print("Geçici veriler silindi!")

zamanBitis = time.time()
surec = zamanBitis-zamanBaslangic
os.system('ren '+fileName+' '+str(int(zamanBaslangic))+"-"+pathName+"."+str(int(surec))+".txt")
print("Dönüştürme tamamlandı!\nİşlem {} saniye sürdü.".format(str(int(surec))))