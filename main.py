from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.core.window import Window


class RVAdvancedApp(App):
    all_items = ListProperty([f"Item {i}" for i in range(1, 51)])
    data_items = ListProperty([])

    def build(self):
        # Load the KV and instantiate the root widget
        root = Builder.load_file('rv_advanced.kv')
        # initialize data_items
        self.data_items = self.all_items.copy()
        return root

    def on_start(self):
        # initial filter
        self.filter_items("")

    def add_item(self):
        txt = self.root.ids.input.text.strip()
        if not txt:
            return
        self.all_items.append(txt)
        self.root.ids.input.text = ""
        self.filter_items(self.root.ids.filter_input.text)

    def remove_item(self, txt):
        if txt in self.all_items:
            self.all_items.remove(txt)
            self.filter_items(self.root.ids.filter_input.text)

    def filter_items(self, q):
        q = q.lower().strip()
        if q:
            self.data_items = [x for x in self.all_items if q in x.lower()]
        else:
            self.data_items = self.all_items.copy()

if __name__ == "__main__":
    RVAdvancedApp().run()   