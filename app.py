import flet as ft
import pyperclip

from src.clases.translate import Translate

def main(page: ft.Page):

    def go_translate(e):        
        
        # Some basic validation
        if len(original.value.replace(" ", "")) == 0:
            return None
        
        # Read the values from the form        
        original_text = original.value
        target_language = e.control.value
        
        # Copy the text translated into the Flet component
        obj = Translate(original_text, target_language)
        translated.value = obj.get_traduction()
        
        # Set some styles to the result
        translated.weight=ft.FontWeight.W_500
        translated.selectable = True
        
        # Establishing functionality to the FloatingActionButton
        if clipboard.on_click == None:
            clipboard.on_click=copy_text            
        
        # Update the page with the new values
        page.update()
        
    # Function to copy on the clipboard    
    def copy_text(e):
        pyperclip.copy(translated.value)
        page.show_snack_bar(
                ft.SnackBar(ft.Text("Text copied on the clipboard"), open=True)
        )
    
    # Set global application settings
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    page.scroll = "adaptive"
    page.title = 'Translated with AI'
    page.window_width = 600
    page.window_height = 400
    
    # Control to type the text to translate
    original = ft.TextField(
                        label="Type text to translate",
                        multiline=True,
                        min_lines=3
                    )
    
    # Control to set the language to be translated
    language_selector = ft.RadioGroup(
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
                            on_change=go_translate
                        )
    
    # Control to show translated text
    translated = ft.Text(
        "Translated text will appear here",
        style=ft.TextThemeStyle.TITLE_MEDIUM,
        font_family="RobotoSlab",
        weight=ft.FontWeight.W_200
    )
    
    # Control for the FloatingActionButton that will copy on the clipboard
    clipboard = ft.FloatingActionButton(
        icon=ft.icons.COPY_OUTLINED,        
        bgcolor=ft.colors.TEAL_300,
        tooltip="Copy Text",
        mini=True,
        # shape=ft.CircleBorder
    )
    
    # Adding the FloatingActionButton to the application
    page.floating_action_button = clipboard
    
    # Adding the rest of the controls to the application    
    page.add(original, language_selector, ft.Divider(), translated)
    
    
ft.app(target=main) 
