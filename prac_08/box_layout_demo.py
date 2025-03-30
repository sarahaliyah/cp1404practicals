from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy application demonstrating BoxLayout with greeting feature."""
    def build(self):
        """Load and return the app interface from the KV file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Process the greeting action. Updates the output label with a personalized message based on user input.
        """
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Reset the input and output fields. Erases the text in both the input field and the output label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
