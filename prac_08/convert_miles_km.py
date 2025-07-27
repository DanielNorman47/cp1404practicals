from kivy.app import App
from kivy.lang import Builder

class MilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """convert miles to km"""
        km_label = self.root.ids.km # store the field object for easier reading
        miles_field = self.root.ids.miles
        km_label.text = str(int(miles_field.text) * 1.60934)
        pass

    def handle_up(self):
        """up button"""
        miles_field = self.root.ids.miles # store the field object for easier reading
        miles_field.text = str(int(miles_field.text) + 1)

    def handle_down(self):
        """down button"""
        miles_field = self.root.ids.miles # store the field object for easier reading
        miles_field.text = str(int(miles_field.text) - 1)


MilesToKm().run()