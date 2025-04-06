import flet as ft

class AnimatedErrorExample(ft.UserControl):
    def build(self):
        self.username_field = ft.TextField(
            label="Usuario",
            hint_text="Escribe tu usuario",
        )

        self.error_text = ft.Text("", color=ft.colors.RED, size=12)
        self.error_container = ft.AnimatedSwitcher(
            child=self.error_text,  # <-- CORRECTO
            transition="fade",
            duration=300,
        )

        self.button = ft.ElevatedButton(text="Validar", on_click=self.validate)

        return ft.Column(
            controls=[
                self.username_field,
                self.error_container,
                self.button
            ],
            spacing=10,
        )

    def validate(self, e):
        value = self.username_field.value.strip()
        if not value.isalpha():
            self.error_container.content.value = "El usuario solo puede contener letras"
        else:
            self.error_container.content.value = ""
        self.error_container.update()

def main(page: ft.Page):
    page.title = "Validación animada"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(AnimatedErrorExample())

ft.app(target=main)
