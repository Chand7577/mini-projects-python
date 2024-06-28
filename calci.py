from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput



class Boxlayout(BoxLayout):     # BoxLayout is a layout or a container that aligns 
                                # its children or sub widgets horizontally or vetically 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.orientation="vertical"

        self.result=TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55
        )
        self.add_widget(self.result)
        
        buttons=[
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','C','+']
        ]
       

        for row in buttons:
            h_layout=BoxLayout()
            for num in row:
                button=Button(text=num,pos_hint={"center_x":0.5,"center_y":0.5})
                button.bind(on_press=self.button_press)
                h_layout.add_widget(button)
        
            self.add_widget(h_layout)

        
        equals_button=Button(text="=",pos_hint={"center_x":0.5,"center_y":0.5})
        equals_button.bind(on_press=self.solution)
        self.add_widget(equals_button)




    def button_press(self,instance):   # instance helps in determining which widget triggered the event 
        currentvalue=self.result.text   #Its similar to event 'e' in javascript 
        button_value=instance.text
        
        if button_value=="C":
            self.result.text=""
        
        else:
            new_text=currentvalue+button_value
            self.result.text=new_text


    def solution(self,instance):
        expression=self.result.text
       

        if expression:
            try:
                self.result.text=str(eval(expression))

            except Exception as e:
                self.result.text="Error"



class Calci(App):
    def build(self):
        return Boxlayout()



if __name__=="__main__":
    Calci().run()