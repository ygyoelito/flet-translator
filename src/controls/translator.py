import flet as ft
from src.clases.translate import Translate

class Translator(ft.UserControl):
    
    text_translate = ""
    
    def build(self):
        # Control to type the text to translate
        self.original = ft.TextField(
                            label="Type text to translate",
                            multiline=True,
                            min_lines=3
                        )
    
        #TODO: Change radios to buttons with the flag of countries
        # Control to set the language to be translated
        self.language_selector = ft.RadioGroup(
                                content=ft.Row(
                                    [
                                        ft.Radio(value="en", label="English"),
                                        ft.Radio(value="es", label="Spanish"),
                                        ft.Radio(value="it", label="Italian"),
                                        ft.Radio(value="ja", label="Japanese"),
                                        ft.Radio(value="ru", label="Russian"),
                                        ft.Radio(value="de", label="German")
                                    ]
                                ),
                                on_change=self.go_translate
                            )
    
        # Control to show translated text
        self.translated = ft.Text(
            "Translated text will appear here",
            style=ft.TextThemeStyle.TITLE_MEDIUM,
            font_family="RobotoSlab",
            weight=ft.FontWeight.W_200
        )
        
        # Container of all controls
        self.displayView = ft.Container(
            content= ft.Column(
                controls=[
                    self.original,
                    self.language_selector,
                    ft.Divider(),
                    self.translated,
                ]
            )
        )
        
        return self.displayView
    
    # Exposes the translated text
    def get_value_translated(self):
        return self.text_translate
        
    # Execute the translation of the selected language
    def go_translate(self, e):        
        
        # Some basic validation
        if len(self.original.value.replace(" ", "")) == 0:
            return None
        
        # Read the values from the form        
        original_text = self.original.value
        target_language = e.control.value
        
        # Copy the text translated into the Flet component
        obj = Translate(original_text, target_language)
        self.translated.value = obj.get_traduction()
        
        # Set some styles to the result
        self.translated.weight=ft.FontWeight.W_500
        self.translated.selectable = True
        
        # Save the text translated into class variable
        self.text_translate = self.translated.value
        
        # Update the page with the new values
        self.translated.update()