"""dynamic labels prac"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]


    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels for each name in a list"""
        for name in self.names:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=name)
            self.root.ids.main.add_widget(temp_button)

DynamicLabelsApp().run()