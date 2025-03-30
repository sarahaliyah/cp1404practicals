from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATE_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """KKivy application for converting miles to kilometers."""
    message = StringProperty()

    def build(self):
        """Build the app interface from the KV file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_update(self):
        """Handle the conversion when the button is pressed."""
        try:
            miles = float(self.root.ids.input_miles.text) if self.root.ids.input_miles.text else 0.0
            kilometers = miles * CONVERSION_RATE_MILES_TO_KM
            self.message = f"{kilometers:.2f} km"
        except ValueError:
            self.root.ids.user_input.text = "0"
            self.handle_update()

    def handle_increment(self, change):
        """Handle the miles value by a given amount and update the result."""
        try:
            miles = float(self.root.ids.input_miles.text) if self.root.ids.input_miles.text else 0.0
            miles += change
            self.root.ids.input_miles.text = str(miles)
            self.update_result(miles)
        except ValueError:
            self.root.ids.input_miles.text = "0"
            self.update_result(0.0)

    def update_result(self, miles):
        """Update and display the recalculated equivalent kilometers"""
        print("update")
        self.message = str(miles * CONVERSION_RATE_MILES_TO_KM)


MilesConverterApp().run()
