from kivy.app import App
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
import pyejdb



class Browser(Widget):
    ludzie=StringProperty("")
    layout = FloatLayout()

    def callback1(instance):
        print('deunisc')

    pass

class EjdbBrowser(App):
    def build(self):
        browser = Browser()
        db = pyejdb.EJDB("city", pyejdb.DEFAULT_OPEN_MODE)
        cursor = db.find("people")
        for entry in cursor:
            browser.ludzie += "=======================\n"
            for fields in entry.items():
                browser.ludzie += ("{0}:{1}".format(fields[0], fields[1])) + "\n"
        print(browser.ludzie)

        return browser

if __name__ == '__main__':
    EjdbBrowser().run()