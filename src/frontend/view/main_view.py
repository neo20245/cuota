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
        self.username_field = CustomTextField(label="Usuario")
        self.password_field = CustomTextField(label="Contraseña", password=True)
        self.save_checkbox = CustomCheckbox(label="Guardar contraseña")

        self.status_message_container = ft.Container(
            content=ft.Text(
                "Proxi iniciado corectamente",
                size=18,
                weight=ft.FontWeight.BOLD,
                color="black",
                text_align=ft.TextAlign.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=15,
            bgcolor="#DFF6DD",
            border_radius=10,
            #          visible=self.show_success,
            animate_opacity=300,
        )

        # Asegúrate de usar un color válido
        self.icon_summit = ft.Icon(ft.icons.PLAY_ARROW, color="white")
        self.submit_button = CustomElevatedButton(self.icon_summit)

        self.progress_ring = ft.ProgressRing(
            color=ft.Colors.INDIGO_500,
            bgcolor="#E0E0E0",
            width=150,
            height=150,
            stroke_width=10,
            value=0.6,
        )
        self.progress_text = ft.Text(
            "40/100", size=20, weight=ft.FontWeight.BOLD, color="black"
        )

    def build_ui(self):
        """Build the full UI layout"""
        layout = CustomControllerBasePage(  # Verifica el nombre correcto aquí
            content=ft.Column(
                controls=[
                    self.status_message_container,
                    self._build_progress_section(),
                    self._build_input_section(),
                    self._build_submit_section(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
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
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def _build_submit_section(self):
        return CustomContainer(
            content=self.submit_button,
        )

    def _build_submit_section2(self):
        self.status_message_container.content = ft.IconButton(
            icon=ft.icons.ARROW_FORWARD,
            icon_color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN_400,
            on_click=self.on_submit,
            tooltip="Enviar",
            icon_size=40,
        )
        return CustomContainer(
            content=self.submit_button_container,
            bgcolor=ft.Colors.AMBER_400,
            height=50,
        )

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

        self._show_status_message()

    def _show_status_message(self):
        """Display connection status message"""
        status = "conectado" if self.app_context.is_connected else "desconectado"
        color = (
            ft.Colors.GREEN_400 if self.app_context.is_connected else ft.Colors.RED_400
        )

        self.status_message_container.content = ft.Text(
            f"Proxy {status} con éxito", color=color, size=20
        )
        self.status_message_container.visible = True

        if self.page:
            self.status_message_container.update()
