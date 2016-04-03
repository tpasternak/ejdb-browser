from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.filechooser import FileChooserController
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os

import pyejdb

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):

    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)


class Browser(Widget):
    people = StringProperty("")
    layout = GridLayout()
    path1 = ''
    already_created = False

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        path1=path
        self._popup.dismiss()

    def dismiss_popup(self):
        self._popup.dismiss()

    def callback(self,treeview,a):
        with pyejdb.EJDB("city", pyejdb.DEFAULT_OPEN_MODE) as db:
            cursor = db.find("people")
            items = []
            for entry in cursor:
                entryString = ""
                for fields in entry.items():
                    entryString += fields[1] + " "
                items.append(entryString)

            if not self.already_created:
                for name in items:
                    yield TreeViewLabel(text=name)

            self.already_created = True

    def callback1(self):
        self.show_load()
    pass


class EjdbBrowser(App):
    def build(self):
        browser = Browser()
        return browser
    Factory.register('Root', cls=Root)
    Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
    EjdbBrowser().run()
