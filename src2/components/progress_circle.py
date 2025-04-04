import flet as ft


class ProgressCircle(ft.Stack):
    def __init__(self):
        super().__init__(
            [
                ft.ProgressRing(
                    value=0.6,
                    color=ft.Colors.RED_500,
                    bgcolor=ft.Colors.GREY_200,
                    width=150,
                    height=150,
                ),
                ft.Container(
                    content=ft.Text(
                        "60%",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                ),
            ],
            width=150,
            height=150,
        )
