import flet as ft
import pyperclip


class CopyButton(ft.UserControl):   
    
    text = ""

    
    def set_text(self, some_text):
        self.text = some_text        
        print(self.text)
    
    #TODO: Create an UserControl for this FloatingctionButton
    # Function to copy on the clipboard    
    def copy_text(self, e):
        print(self.text)       
        
        # if control.get_value_translated() != "":
        #     pyperclip.copy(control.get_value_translated())
        #     page.show_snack_bar(
        #             ft.SnackBar(ft.Text("Text copied on the clipboard"), open=True)
        #     )
        
        # if self.text != "":
        #     pyperclip.copy(self.text)
        #     ft.page.show_snack_bar(
        #             ft.SnackBar(ft.Text("Text copied on the clipboard"), open=True)
        #     )
        
        
    
    
    # Control for the FloatingActionButton that will copy on the clipboard
    def build(self):
        self.clipboard = ft.FloatingActionButton(
            icon=ft.icons.COPY_OUTLINED,        
            bgcolor=ft.colors.TEAL_300,
            tooltip="Copy Text",
            mini=True,
            on_click=self.copy_text,
            shape=ft.CircleBorder()
        )

        return self.clipboard