import flet as ft
from frontend.view.main_controller import MainController


def main(page: ft.Page):
    # Crear la vista principal que controlará la aplicación
    MainController(page)


# Punto de entrada de la aplicación
if __name__ == "__main__":
    ft.app(target=main)
else:
    # Para casos donde este módulo pueda ser importado
    ft.app(target=main)
