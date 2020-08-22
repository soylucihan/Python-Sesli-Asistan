
#-*- coding: utf-8 -*-
import speech_recognition as sr
import os
import time
from gtts import gTTS
 
#Bu bizim konuşma fonksiyonumuz her speak("text") tetiklendiğinde aldığı değer için Text to Speech Yapacak.
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='tr')
    tts.save("audio.mp3")
    os.system("audio.mp3")

#Bu ise mikrofonumuzu dinleyen fonksiyonumuz
def recordAudio():#Mikrofonu dinlemeden önce Recognizer(tanıyıcı)mızı tanımlıyoruz.
    r = sr.Recognizer()
    #Burada mikrofondan veri almaya başlıyoruz
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Burada google'ın ses tanıma sistemini kullandık bu sistem internet gerektiriyor.
    data = ""
    
    try:
        #burda türkçe olmasını istediğimiz için tanıyıcımızın türkçe sesleri tanımasını ayarlıyoruz.
        data = r.recognize_google(audio, language='tr-tr')
        #burada sesinizin tonuna göre büyük küçük harf geldiği için text verisini lower hale getiriyoruz. 
        data= data.lower()
    #Bu ise gereksiz gürültü sesleri geldiğinde döndüreceği komut
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
    return data
 
#Burada ise fonksiyona verilen metin içerisinde yakalanan metinler komut mu diye kontrol ediliyor 
def asistan(data):#Eğer yakalanan metin merhaba ise asistan bize Merhaba Emre sesini döndürecek.
#Buraya daha fazla şey ekleyebilirsiniz.
    if "merhaba" in data:
        speak("Merhaba cihan")

#Asistanı Başlatmadan 2 Saniye bekleyip, Text to Speech yaptırıyoruz.
    time.sleep(2)
    speak("Merhaba cihan, Sana Nasıl Yardımcı Olabilirim?")

#Bu kısımda sürekli dinlemesini sağlamak için sonsuz döngü içerisine sokuyoruz.
while 1:
    data = recordAudio()
    asistan(data)