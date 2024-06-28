from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput


class Userinterface(GridLayout):

    def __init__(self,**kwargs):

        super(Userinterface,self).__init__(**kwargs)

        self.cols=2
        

        self.add_widget(Label(text=""))
        self.userInput=TextInput(multiline=False)
        self.add_widget(self.userInput)
        
        # adding button
       
        self.btn1=Button(text="1")
        self.btn1.bind(on_press=self.say_something)
        self.add_widget(self.btn1)

        self.btn2=Button(text="2")
        self.btn2.bind(on_press=self.say_something)
        self.add_widget(self.btn2)

        self.btn3=Button(text="3")
        self.btn3.bind(on_press=self.say_something)
        self.add_widget(self.btn3)
        
        self.btn4=Button(text="4")
        self.btn4.bind(on_press=self.say_something)
        self.add_widget(self.btn4)
        
        self.btn5=Button(text="5")
        self.btn5.bind(on_press=self.say_something)
        self.add_widget(self.btn5)
        
        self.btn6=Button(text="6")
        self.btn6.bind(on_press=self.say_something)
        self.add_widget(self.btn6)
        
        self.btn7=Button(text="7")
        self.btn7.bind(on_press=self.say_something)
        self.add_widget(self.btn7)

        self.btn8=Button(text="8")
        self.btn8.bind(on_press=self.say_something)
        self.add_widget(self.btn8)

        self.btn9=Button(text="9")
        self.btn9.bind(on_press=self.say_something)
        self.add_widget(self.btn9)

    def say_something(self,instance):
       
        self.add_widget(TextInput(self.userinfo)
        
        self.userInput.text=""




class MyApp(App):
    def build(self):
        return Userinterface()



if __name__=="__main__":
    MyApp().run()
