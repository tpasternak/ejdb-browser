from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.filechooser import FileChooserController


import pyejdb


class Browser(Widget):
    people = StringProperty("")
    layout = FloatLayout()

    def button1(self):
        print("Button 1 triggered")

    def callback(treeview,a,b):
        with pyejdb.EJDB("city", pyejdb.DEFAULT_OPEN_MODE) as db:
            cursor = db.find("people")
            items = []
            for entry in cursor:
                entryString = ""
                for fields in entry.items():
                    entryString += fields[1] + " "
                items.append(entryString)

            for name in items:
                yield TreeViewLabel(text=name)

    def callback1(instance):
        print('deunisc')

    pass

class EjdbBrowser(App):
    def build(self):
        browser = Browser()

        return browser

if __name__ == '__main__':
    EjdbBrowser().run()
