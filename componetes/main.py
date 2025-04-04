import flet as ft
from comp import CustomTextField


def main(page: ft.Page):
    page.title = "Contenedor App"

    # Crear un contenedor
    text_field = CustomTextField("sdf")

    # Añadir el contenedor a la página
    page.add(text_field)


if __name__ == "__main__":
    ft.app(target=main)
