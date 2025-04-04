import flet as ft


class SuccessMessage(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Icon(
                                ft.icons.CHECK_CIRCLE,
                                color=ft.Colors.GREEN_700,
                                size=30,
                            ),
                            ft.Text(
                                "Proxy Iniciado correctamente",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                ),
                elevation=8,
            ),
            visible=False,
            alignment=ft.alignment.top_center,
        )

    def show_message(self):
        self.visible = True
