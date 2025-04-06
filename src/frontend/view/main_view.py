import flet as ft
from backend.app_context import AppContext
from frontend.ui_components import (
    CustomControllerBasePage,  # Verifica el nombre correcto aquí
    CustomContainer,
    CustomCheckbox,
    CustomTextField,
    CustomElevatedButton,
)


class MainViewPage:
    def __init__(self, page: ft.Page):
        self.app_context = AppContext()
        self.page = page
        self._init_ui_components()

    def _init_ui_components(self):
        """Initialize UI components"""
        self.username_field = CustomTextField(
            label="Usuario",
            hint_text="Escribe el nombre de usuario",
            prefix_icon=ft.Icons.PERSON,
        )
        self.password_field = CustomTextField(
            label="Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
        )
        self.save_checkbox = CustomCheckbox(label="Guardar contraseña")

        self.status_message_container = ft.Card(
            content=CustomContainer(
                content=ft.Text(
                    "Nombre de usuario o contraseña están incorrectos, revise la conexión",
                    italic=True,
                    size=16,
                    color="white",
                    text_align=ft.TextAlign.CENTER,
                ),
                padding=20,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#6a11cb", "#2575fc"],  # degradado bonito
                ),
                # Borde fino blanco
                border_radius=10,
                expand=True,  # Hace que el CustomContainer ocupe todo el espacio disponible
            ),
            opacity=0.0,  # Inicialmente invisible
            elevation=6,
            margin=ft.margin.symmetric(vertical=8),  # sin márgenes laterales
            animate_opacity=500,  # Animación de opacidad
        )

        # Submit button
        self.icon_summit = ft.Icon(ft.icons.PLAY_ARROW, color=ft.Colors.WHITE, size=40)
        self.submit_button = CustomElevatedButton(
            content=ft.Row(
                controls=[self.icon_summit],
            ),
            on_click=self.on_submit,
            bgcolor=ft.Colors.INDIGO_500,
        )

        self.progress_ring = ft.ProgressRing(
            color=ft.Colors.INDIGO_500,
            bgcolor="#E0E0E0",
            width=150,
            height=150,
            stroke_width=10,
            value=0.6,
        )
        self.progress_text = ft.Text(
            "40/100", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_500
        )

    def build_ui(self):
        """Build the full UI layout"""
        layout = CustomControllerBasePage(
            content=ft.Column(
                controls=[
                    self.status_message_container,  # Asegúrate de mantenerlo en la misma posición
                    self._build_progress_section(),
                    self._build_input_section(),
                    self._build_submit_section(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=4,
            )
        )
        return layout

    def _build_progress_section(self):
        return CustomContainer(
            content=ft.Stack(
                controls=[self.progress_ring, self.progress_text],
                expand=True,
                alignment=ft.alignment.center,
            ),
            padding=6,
        )

    def _build_input_section(self):
        return CustomContainer(
            content=ft.Column(
                controls=[
                    self.username_field,
                    self.password_field,
                    ft.Container(
                        content=self.save_checkbox,
                        alignment=ft.alignment.center,
                        width=250,
                        margin=0,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=6,
            ),
            height=170,
        )

    def _build_submit_section(self):
        return CustomContainer(content=self.submit_button)

    def on_submit(self, e):
        """Handle the submit button click"""
        user = self.username_field.value
        password = self.password_field.value
        save = self.save_checkbox.value

        print(f"Usuario: {user}")
        print(f"Contraseña: {password}")
        print(f"Guardar contraseña: {save}")

        self.app_context.user = user
        self.app_context.password = password
        self.app_context.is_connected = not self.app_context.is_connected

        # Mostrar el mensaje de estado cambiando la opacidad
        self.status_message_container.opacity = (
            1.0 if self.app_context.is_connected else 0.0
        )
        self.page.update()

    def _show_status_message(self):
        """Display connection status message"""
        status = "conectado" if self.app_context.is_connected else "desconectado"
        color = (
            ft.Colors.GREEN_400 if self.app_context.is_connected else ft.Colors.RED_400
        )

        self.status_message_container.content = ft.Text(
            f"Proxy {status} con éxito", color=color, size=20
        )
        self.status_message_container.opacity = 1.0  # Mostrar el mensaje de estado
        if self.page:
            self.status_message_container.update()
