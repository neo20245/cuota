import flet as ft


class SavePasswordCheckbox(ft.Checkbox):
    def __init__(self):
        super().__init__(
            label="Guardar Contraseña",
            value=True,
            check_color=ft.Colors.WHITE,
            fill_color=ft.Colors.BLACK,
        )
