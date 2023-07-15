from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ListProperty
import csv

Builder.load_string("""
<Test>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    BoxLayout:
        Label:
            text:'list 1'
        Label:
            text:'label 2'
"""
)

class Test(BoxLayout):
    label_value = ListProperty()
    #testList= ['potato', 'jake', 'ofu', 'zach']
    def __init__(self, **kw):
        super(Test, self).__init__(**kw)
        testlist = open('/Users/HOME/Desktop/Hackaton/Result/Loss_Data.csv', encoding='UTF8').read()
        #reads in data
        zach_list = testlist.split("\n")
        item_count= 1
        for value in zach_list:
            btn= Button(text= str(value), pos=(100,10))
            label= Label(text=str(item_count) )
            item_count= item_count + 1
            #self.rows= rows
            self.add_widget(label)
            self.add_widget(btn)


class TestApp(App):
    def build(self):
        return Test()

TestApp().run()