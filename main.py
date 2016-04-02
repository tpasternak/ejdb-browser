from kivy.app import App
from kivy.uix.widget import Widget
import pyejdb
from kivy.properties import StringProperty

from kivy.uix.treeview import TreeViewLabel


class Browser(Widget):
    people=StringProperty("")
    already_created = False

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

    pass


class EjdbBrowser(App):
    def build(self):
        browser = Browser()

        return browser

if __name__ == '__main__':
    EjdbBrowser().run()
