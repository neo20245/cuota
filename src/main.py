import flet as ft
from frontend.main_controller import MainController


def main(page: ft.Page):
    MainController(page)


ft.app(target=main)
