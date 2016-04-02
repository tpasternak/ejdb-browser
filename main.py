from kivy.app import App
from kivy.uix.widget import Widget
import pyejdb
from kivy.properties import StringProperty

from kivy.uix.treeview import TreeViewLabel


class Browser(Widget):
    ludzie=StringProperty("")

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

    pass


class EjdbBrowser(App):
    def build(self):
        browser = Browser()
#        db = pyejdb.EJDB("city", pyejdb.DEFAULT_OPEN_MODE)
#        cursor = db.find("people")

#        for entry in cursor:
#            browser.ludzie += "=======================\n"
#            for fields in entry.items():
#                browser.ludzie += ("{0}:{1}".format(fields[0], fields[1])) + "\n"
#        print(browser.ludzie)

        return browser

if __name__ == '__main__':
    EjdbBrowser().run()