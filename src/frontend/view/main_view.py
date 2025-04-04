
import flet as ft
from frontend.ui_components import (
    CustomTextField,
    CustomContolerBasePage,
    CustomContainer,
    CustomCheckbox,
)


class MainViewPage:
    @staticmethod
    def build_ui():
        return CustomContolerBasePage(
            content=ft.Column(
                controls=[
                    # contenedor del usuario / pass y save pass
                    CustomContainer(
                        content=ft.Column(
                            controls=[
                                CustomTextField(label="Usuasdfrdfgio"),
                                CustomTextField(label="Contrasena"),
                                # Envuelve el CustomCheckbox en un Container con alineación centrada
                                ft.Container(
                                    content=CustomCheckbox(
                                        label="Guardar Contrasena",
                                    ),
                                    alignment=ft.alignment.center,
                                    width=250  # Mismo ancho que los TextField
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.colors.RED_500,  # Usa colors en minúscula
                    ),
                    CustomContainer(content=ft.ElevatedButton(text="Submit")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
