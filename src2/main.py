import flet as ft
from components.success_message import SuccessMessage
from components.progress_circle import ProgressCircle
from components.input_fields import InputFields
from components.play_button import PlayButton
from components.checkbox import SavePasswordCheckbox


class CuotaUCIApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.show_success = (
            False  # Estado para controlar la visibilidad del mensaje de éxito
        )
        self.setup_page()
        self.create_components()
        self.build_layout()

    def setup_page(self):
        """Configura las propiedades de la página."""
        self.page.title = "Cuota UCI"
        self.page.bgcolor = ft.Colors.WHITE
        self.page.window.width = 400  # Simular pantalla móvil
        self.page.window.height = 700
        self.page.window.resizable = False
        self.page.padding = 0

    def on_play_click(self, e):
        """Maneja el evento de clic en el botón de play."""
        self.show_success = True
        self.success_card.show_message()  # Mostrar la tarjeta
        self.page.update()

    def create_components(self):
        """Crea todos los componentes de la interfaz."""
        self.success_card = SuccessMessage()
        self.progress_circle = ProgressCircle()
        self.input_fields = InputFields()
        self.checkbox = SavePasswordCheckbox()
        self.play_button = PlayButton(self.on_play_click)

    def build_layout(self):
        """Construye el diseño de la aplicación."""
        main_column = ft.Column(
            [
                ft.Container(
                    content=self.success_card, alignment=ft.alignment.top_center
                ),  # Ahora el mensaje de éxito está antes del círculo de progreso
                ft.Container(
                    content=self.progress_circle, alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Column(
                        [*self.input_fields.get_fields(), self.checkbox],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Container(
                    content=self.play_button,
                    alignment=ft.alignment.bottom_center,
                    padding=ft.padding.only(bottom=20),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            expand=True,
        )
        self.page.add(main_column)


def main(page: ft.Page):
    CuotaUCIApp(page)


ft.app(target=main)
