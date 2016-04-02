from kivy.app import App
from kivy.uix.widget import Widget
import pyejdb
from kivy.properties import StringProperty
class Browser(Widget):
    ludzie=StringProperty("")

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