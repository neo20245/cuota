import flet as ft


class PlayButton(ft.ElevatedButton):
    def __init__(self, on_click):
        super().__init__(
            content=ft.Icon(ft.icons.PLAY_ARROW, size=30, color=ft.Colors.WHITE),
            style=ft.ButtonStyle(
                shape=ft.CircleBorder(),
                bgcolor=ft.Colors.BLUE_500,
                padding=15,
            ),
            width=60,
            height=60,
            on_click=on_click,
        )
