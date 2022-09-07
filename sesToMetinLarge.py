# importing libraries
import time 
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
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
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

# Ses dosyası seç
root = tk.Tk()
root.withdraw()

# dosya yolu oluştur
file_path = filedialog.askopenfilename(filetypes=[("Ses dosyaları",".wav .aiff .aif .aifc .flac")])

'''
path = "TUBITAK2219_ADEMPOLAT.wav"
print("\nFull text:", get_large_audio_transcription(file_path))
'''
result = get_large_audio_transcription(file_path)

# Metni dosyaya kaydet
pathName = Path(file_path)
pathName = pathName.name
fileName = str(int(time.time()))+"-"+pathName+".txt"
f = codecs.open(fileName, "a", "utf-8")
f.write(result)
f.close()

# Oluşturulan dosya içeriğini dosyayı terminalde göster
f = open(fileName, "r", encoding='utf-8')
print("\nFull text: ")
print(f.read())