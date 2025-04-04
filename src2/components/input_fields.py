import flet as ft


class InputFields:
    def __init__(self):
        self.text_field_1 = ft.TextField(
            hint_text="Usuario",
            hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
            border_color=ft.Colors.GREY_400,
            border_radius=10,
            width=300,
            bgcolor=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.BLACK),
            filled=True,
        )

        self.text_field_2 = ft.TextField(
            hint_text="Contraseña",
            hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
            border_color=ft.Colors.GREY_400,
            border_radius=10,
            width=300,
            bgcolor=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.BLACK),
            password=True,
            filled=True,
        )

    def get_fields(self):
        return [self.text_field_1, self.text_field_2]
