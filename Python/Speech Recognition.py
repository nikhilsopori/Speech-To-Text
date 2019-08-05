#Installing of the Python Package

#**Note that the SpeechRecoginition will only work for Python (2,2.7,3,3.3,3.4,3.5,3.6)

!pip install SpeechRecognition
!pip install librosa
!pip install soundfile


#Import Speech Recognition Package
import speech_recognition as sr
import librosa
import soundfile as sf
import wave

r = sr.Recognizer()

#Librosa is Used for Converting MP3 file into wav or any audio type
x,_= librosa.load('BANNERS - Start A Riot.mp3',sr=16000)
sf.write('temp.wav',x,16000)


audio =  sr.AudioFile("temp.wav")
print("......... Running ")

with audio as text:
    text1 = r.record(text,offset=10,duration=400)
print(r.recognize_google(text1))
