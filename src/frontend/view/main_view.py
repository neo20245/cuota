import flet as ft
from backend.app_context import AppContext
from frontend.flet_validations import FletValidator as flet_validator
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
            disable=self.app_context.is_connected,
            on_blur=self._on_usernmae_blur,



        )
        self.password_field = CustomTextField(
            label="Contraseña",
            password=True,
            hint_text="escribe la contrasena",
            prefix_icon=ft.Icons.LOCK,
            can_reveal_password=True,
            disable=self.app_context.is_connected,
            on_blur=self._on_password_blur
        )
        self.save_checkbox = CustomCheckbox(label="Guardar contraseña",disabled=self.app_context.is_connected)

        self.status_message_container = ft.Card(
            content=CustomContainer(
                content=ft.Text(
                    "Nombre de usuario o contraseña están incorrectos, revise la conexión",
                    italic=True,
                    size=16,
                    color="white",
                    text_align=ft.TextAlign.CENTER,
                ),
                padding=10,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#6a11cb", "#2575fc"],  # degradado bonito
                ),
                # Borde fino blanco
                border_radius=10,
                expand=True,  # Hace que el CustomContainer ocupe todo el espacio disponible
                alignment=ft.alignment.center
            ),
            opacity=0.0,  # Inicialmente invisible
            elevation=6,
            margin=ft.margin.symmetric(vertical=8),  # sin márgenes laterales
            animate_opacity=100,  # Animación de opacidad
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
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=10,
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
            alignment= ft.alignment.center

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
                spacing=12,
            ),
            height=210,
             alignment= ft.alignment.center
        )

    def _build_submit_section(self):
        ft.alignment.bottom_center
        return CustomContainer(content=self.submit_button,alignment=ft.alignment.center)
# validatios
    def _on_usernmae_blur(self, e):
        print("sdfsdf")
        is_valid = flet_validator.validate_username(str(self.username_field.value))
        self.username_field.error_text = "Usuario No valido" if not is_valid else None


    def _on_password_blur(self, e):

        is_valid = flet_validator.validate_password(str(self.password_field.value))
        print(is_valid)
        self.password_field.error_text = "La contraseña debe tener al menos 8 caracteres." if not is_valid else None


    def on_submit(self, e):
        username = str(self.username_field.value).strip()
        password = str(self.password_field.value).strip()

        # Validar username
        if not flet_validator.validate_username(username):
            self.username_field.error_text = ("Usuario no válido"
)
        # Validar password
        if not flet_validator.validate_password(password):
            self.password_field.error_text = "Contraseña no válida"


        self.page.update()

        # Verificar si todo está correcto
        if self.username_field.error_text is None and self.password_field.error_text is None:
            print("Todo OK, enviando...")
            # Tu lógica de autenticación o lo que necesites
        else:
            print("Errores en el formulario")






        # self.app_context.user = self.username_field.value
        # self.app_context.password = self.password_field.value
        # self.app_context.is_connected = not self.app_context.is_connected

        # Mostrar el mensaje de estado cambiando la opacidad
        self.status_message_container.opacity = (
            1.0 if self.app_context.is_connected else 0.0
        )
        self.page.update()
