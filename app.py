import flet as ft
import pyperclip

from src.controls.translator import Translator

def main(page: ft.Page):

    control = Translator()
    
    
    
    # Set global application settings
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    page.scroll = "adaptive"
    page.title = 'Translated with AI'
    page.window_width = 600
    page.window_height = 400
    
    #TODO: Create an UserControl for this FloatingctionButton
    # Function to copy on the clipboard    
    def copy_text(e):        
        if control.get_value_translated() != "":
            pyperclip.copy(control.get_value_translated())
            page.show_snack_bar(
                    ft.SnackBar(ft.Text("Text copied on the clipboard"), open=True)
            )
    
    # Control for the FloatingActionButton that will copy on the clipboard
    clipboard = ft.FloatingActionButton(
        icon=ft.icons.COPY_OUTLINED,        
        bgcolor=ft.colors.TEAL_300,
        tooltip="Copy Text",
        mini=True,
        on_click=copy_text,
        shape=ft.CircleBorder()
    )
    
    # Adding the FloatingActionButton to the application
    page.floating_action_button = clipboard   
    
    page.add(control)
    page.update()
    
ft.app(target=main) 
