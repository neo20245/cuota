import flet as ft
from flet.core.border_radius import horizontal
from frontend.components.flet_componets import (
    CustomTextField,
    CustomContainer,
    CustomContainerPage,
    CustomCheckBox,
)


class MainViewPage:
    def build_ui(self):
        return CustomContainerPage(
            content=ft.Column(
                controls=[
                    # Container del user y pass
                    CustomContainer(
                        content=ft.Stack(
                            controls=[
                                ft.Container(
                                    content=ft.ProgressRing(
                                        width=200,
                                        height=200,
                                        stroke_width=8,
                                        value=0.1,  # 40/400 = 0.1
                                        color=ft.Colors.BLUE,
                                        bgcolor=ft.Colors.BLUE_100,
                                    ),
                                    alignment=ft.alignment.center,
                                    padding=10,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "40/400",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.BLUE_900,
                                    ),
                                    alignment=ft.alignment.center,
                                    padding=10,
                                ),
                            ],
                            width=200,
                            height=200,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    CustomContainer(
                        content=ft.Column(
                            controls=[
                                CustomTextField(label="Usuario"),
                                CustomTextField(
                                    label="Contraseña",
                                    password=True,
                                    prefix_icon=ft.Icons.PASSWORD,
                                    hint_text="Ingrese su contraseña",
                                    hint_style=ft.TextStyle(color=ft.Colors.RED),
                                ),
                                CustomCheckBox(
                                    label="Guardar Contrasena",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente los elementos de la columna
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                    CustomContainer(content=ft.Icons.PLAY_ARROW),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            )
        )
