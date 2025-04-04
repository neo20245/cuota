import flet as ft


class CustomTextField(ft.TextField):
    def __init__(self, text, *kwargs):
        super().__init__(*kwargs)
        self.label = text
        self.border_radius = 8
        self.height = 45
        self.width = 200
        self.bgcolor = ft.Colors.BLACK54  # Fondo negro menos fuerte
        self.color = ft.Colors.WHITE
        self.label_style = ft.TextStyle(
            color=ft.Colors.BLUE_300,
            weight=ft.FontWeight.BOLD,
            size=14,
        )
        self.cursor_color = ft.Colors.RED  # Cursor color rojo
        self.cursor_width = 1
        self.cursor_height = 18
        # Fix for border property - using outline instead
        self.border_color = ft.Colors.RED  # Color de borde rojo
        self.focused_border_color = ft.Colors.RED  # Color de borde rojo al enfocar
        self.focused_bgcolor = (
            ft.Colors.BLACK54
        )  # Mantener fondo negro menos fuerte al enfocar
        self.content_padding = ft.padding.only(left=16, right=16, top=8, bottom=8)
        self.text_size = 16
        self.text_style = ft.TextStyle(
            color=ft.Colors.AMBER_300,  # Otro color para el texto
            weight=ft.FontWeight.W_500,
        )
        self.autofocus = True
