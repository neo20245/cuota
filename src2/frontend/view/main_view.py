import flet as ft
from backend.app_context import AppContext
from frontend.ui_components import (
    CustomTextField,
    CustomContolerBasePage,
    CustomContainer,
    CustomCheckbox,
)

# Constants for UI labels and styles
LABEL_USERNAME = "Usuario"
LABEL_PASSWORD = "Contraseña"
LABEL_SAVE_PASSWORD = "Guardar Contraseña"
COLOR_CONNECTED = ft.colors.GREEN_400
COLOR_DISCONNECTED = ft.colors.RED_400
ICON_CONNECTED = ft.icons.ARROW_FORWARD
ICON_DISCONNECTED = ft.icons.STOP

class MainViewPage:
    def __init__(self, page: ft.Page):
        self.app_context = AppContext()
        self.page = page
        self._init_ui_components()

    @property
    def is_connected(self) -> bool:
        return self.app_context.is_connected

    def _init_ui_components(self):
        """Initialize UI components"""
        self.username_field = CustomTextField(label=LABEL_USERNAME)
        self.password_field = CustomTextField(label=LABEL_PASSWORD, password=True)
        self.save_checkbox = CustomCheckbox(label=LABEL_SAVE_PASSWORD)

        self.status_message_container = ft.Container(visible=False)
        self.submit_button_container = ft.Container()

        self.progress_ring = ft.ProgressRing(
            color=ft.Colors.RED_50,
            width=170,
            height=170,
            stroke_width=10,
            value=0.5,
            tooltip="0.4",
        )
        self.progress_text = ft.Text(value="0", size=30, color=ft.Colors.RED_300)

    def build_ui(self):
        """Build the full UI layout"""
        layout = CustomContolerBasePage(
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
        self.refresh_ui_state()
        return layout

    def _build_progress_section(self):
        return CustomContainer(
            content=ft.Stack(
                controls=[self.progress_ring, self.progress_text],
                expand=True,
                alignment=ft.alignment.center,
            ),
            bgcolor=ft.colors.BLUE_100,
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
            bgcolor=ft.colors.RED_500,
        )

    def _build_submit_section(self):
        return CustomContainer(
            content=self.submit_button_container,
            bgcolor=ft.Colors.AMBER_400,
            height=50,
        )

    def refresh_ui_state(self):
        """Refresh the UI based on connection state"""
        self._update_input_fields()
        self._update_submit_button()

    def _update_input_fields(self):
        inputs_disabled = self.is_connected
        self.username_field.disabled = inputs_disabled
        self.password_field.disabled = inputs_disabled
        self.save_checkbox.disabled = inputs_disabled

        if self.page:
            self.username_field.update()
            self.password_field.update()
            self.save_checkbox.update()

    def _update_submit_button(self):
        icon = ICON_CONNECTED if self.is_connected else ICON_DISCONNECTED
        color = COLOR_CONNECTED if self.is_connected else COLOR_DISCONNECTED

        self.submit_button_container.content = ft.IconButton(
            icon=icon,
            icon_color=ft.colors.WHITE,
            bgcolor=color,
            on_click=self.on_submit,
            tooltip="Enviar",
            icon_size=40,
        )
        if self.page:
            self.submit_button_container.update()

    def on_submit(self, e):
        """Handle submit button click"""
        user = self.username_field.value
        password = self.password_field.value
        save = self.save_checkbox.value
       
        print(f"Usuario: {user}")
        print(f"Contraseña: {password}")
        print(f"Guardar contraseña: {save}")

        self.app_context.user = user
        self.app_context.password = password
        self.app_context.is_conected = not self.app_context.is_conected

        self._show_status_message()

    def _show_status_message(self):
        """Display connection status message"""
        status = "conectado" if self.is_connected else "desconectado"
        color = COLOR_CONNECTED if self.is_connected else COLOR_DISCONNECTED

        self.status_message_container.content = ft.Text(
            f"Proxy {status} con éxito", color=color, size=20
        )
        self.status_message_container.visible = True

        if self.page:
            self.status_message_container.update()
