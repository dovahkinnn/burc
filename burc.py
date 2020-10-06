
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import requests
from bs4 import BeautifulSoup
import re
class Yazbel(App):


        def build(self):

 
                self.yazi=Label(text = "merhaba",font_size = "12sp",halign = "center")
                self.govde = BoxLayout(orientation = "vertical")

                
                self.buton = Button(text = "Tıkla",size_hint_y = .3)

                self.buton.bind(on_press = self.press)
             

           
                self.govde.add_widget(self.yazi)
                self.govde.add_widget(self.buton)

                return self.govde

        def press(self,q):
                r = requests.get('https://www.gunlukburc.net/gunluk-burc-yorumlari/yay.html')
                source = BeautifulSoup(r.content,"lxml")
                a=source.find("p").text
                s=a.split(".")
                for q in s :
                        print(q)
                        w = Label(text = q,font_size = "14sp",halign = "center")
                        self.govde.add_widget(w)
                
               


Yazbel().run()                