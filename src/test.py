import flet as ft


class CuotaUCIApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.show_success = False  # Estado del mensaje de éxito
        self.setup_page()
        self.create_components()
        self.build_layout()

    def setup_page(self):
        self.page.title = "Cuota UCI"
        self.page.bgcolor = "#F4F4F4"
        self.page.window_width = 400
        self.page.window_height = 700
        self.page.window_resizable = False
        self.page.padding = 10

    def create_success_card(self):
        return ft.Container(
            content=ft.Text(
                "Proxi Iniciado correctamente",
                size=18,
                weight=ft.FontWeight.BOLD,
                color="black",
                text_align=ft.TextAlign.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=15,
            bgcolor="#DFF6DD",
            border_radius=10,
            visible=self.show_success,
            animate_opacity=300,
        )

    def create_progress_circle(self):
        return ft.Stack(
            [
                ft.ProgressRing(
                    value=0.6, color="#D32F2F", bgcolor="#E0E0E0", width=150, height=150
                ),
                ft.Container(
                    content=ft.Text(
                        "60%", size=30, weight=ft.FontWeight.BOLD, color="black"
                    ),
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                ),
            ],
            width=150,
            height=150,
        )

    def create_text_fields(self):
        return [
            ft.TextField(
                label="Usuario",
                width=300,
                border_radius=10,
                filled=True,
                bgcolor="white",
            ),
            ft.TextField(
                label="Contraseña",
                width=300,
                border_radius=10,
                filled=True,
                bgcolor="white",
                password=True,
            ),
        ]

    def create_checkbox(self):
        return ft.Checkbox(label="Guardar Contraseña", value=True)

    def create_play_button(self):
        return ft.ElevatedButton(
            content=ft.Icon(ft.icons.PLAY_ARROW, size=30, color="white"),
            style=ft.ButtonStyle(
                shape=ft.CircleBorder(), bgcolor="#1976D2", padding=15
            ),
            width=60,
            height=60,
            on_click=self.on_play_click,
        )

    def on_play_click(self, e):
        self.show_success = True
        self.success_card.visible = True
        self.page.update()

    def create_components(self):
        self.success_card = self.create_success_card()
        self.progress_circle = self.create_progress_circle()
        self.text_fields = self.create_text_fields()
        self.checkbox = self.create_checkbox()
        self.play_button = self.create_play_button()

    def build_layout(self):
        self.page.add(
            ft.Column(
                [
                    self.success_card,
                    self.progress_circle,
                    *self.text_fields,
                    self.checkbox,
                    ft.Container(
                        content=self.play_button, alignment=ft.alignment.center
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )


def main(page: ft.Page):
    CuotaUCIApp(page)


ft.app(target=main)
