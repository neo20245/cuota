import flet as ft
from frontend.view.main_view import MainViewPage
from backend.app_context import AppContext
from frontend.view.titlebar import create_titlebar  # Importa la función de titlebar


class MainController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_context = AppContext()
        self.configure_view()
        self.build_ui()

    def configure_view(self):
        self.page.window.width = 330
        self.page.window.height = 585
        self.page.padding = 0
        self.title_bar_buttons_hidden = True
        self.title_bar_hidden = True
        self.page.window.title_bar_hidden = True
        self.page.window.title_bar_buttons_hidden = True
        self.page.window.frameless = False
        self.page.bgcolor= ft.Colors.BROWN_50

    def build_ui(self):
        self.main_view = MainViewPage(page=self.page)
        self.page.add(create_titlebar(self.page), self.main_view.build_ui())

        # Añadir la barra de título a la página
        # Llamada a la función para crear la barra de título
